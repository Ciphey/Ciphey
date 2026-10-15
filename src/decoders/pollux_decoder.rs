//! Pollux cipher decoder
//!
//! Pollux encodes Morse code by replacing every `.` with one digit from {1, 4, 7}, every
//! `-` with one digit from {2, 5, 8}, and every separator (between elements of a symbol
//! and between symbols) with one digit from {3, 6, 9, 0}. Each digit class picks one
//! digit per Morse character. No separators appear in the ciphertext: Pollux splits the
//! digit stream on the run length of the symbol the digit stands for. The result is a
//! string of digits that looks random.
//!
//! Ciphey's Pollux cracker brute-forces the assignment of digits to {`.`, `-`,
//! separator}, builds the Morse string, decodes it through [`MorseCodeDecoder`], and
//! reports the first reading that Athena accepts at low sensitivity (the convention for
//! classical ciphers).
//!
//! Only 3¹⁰ = 59,049 assignments exist, so the search is bounded.

use crate::checkers::CheckerTypes;
use crate::decoders::interface::{Crack, Decoder};
use crate::decoders::morse_code::MorseCodeDecoder;
use gibberish_or_not::Sensitivity;
use log::trace;

use super::crack_results::CrackResult;

/// One Pollux class: which Morse symbol the digit stands for.
#[derive(Clone, Copy, PartialEq, Eq)]
enum PolluxClass {
    /// A Morse dot
    Dot,
    /// A Morse dash
    Dash,
    /// A separator between elements or symbols
    Sep,
}

impl PolluxClass {
    /// The Morse character that stands for this class.
    fn symbol(self) -> char {
        match self {
            PolluxClass::Dot => '.',
            PolluxClass::Dash => '-',
            // MorseCodeDecoder splits on a single ASCII space and treats `/` as a word
            // separator too; space is what comes out of a Pollux separator.
            PolluxClass::Sep => ' ',
        }
    }
}

/// Pollux decoder
pub struct PolluxDecoder;

impl Crack for Decoder<PolluxDecoder> {
    fn new() -> Decoder<PolluxDecoder> {
        Decoder {
            name: "pollux",
            description: "Decodes the Pollux cipher, which encodes Morse code by replacing dots, dashes and separators with single digits from three disjoint classes (1/4/7, 2/5/8 and 3/6/9/0). Tries every assignment of digits to the three classes (3^10 = 59049 possibilities) and reports the first reading that passes the checker. Uses Low sensitivity for gibberish detection.",
            link: "https://en.wikipedia.org/wiki/Pollux_(cipher)",
            tags: vec!["pollux", "morse", "cipher", "classic", "substitution"],
            popularity: 0.4,
            phantom: std::marker::PhantomData,
        }
    }

    fn crack(&self, text: &str, checker: &CheckerTypes) -> CrackResult {
        trace!("Trying PolluxDecoder with text {:?}", text);
        let mut results = CrackResult::new(self, text.to_string());

        // Pollux only takes digits; reject anything else without iterating 59k
        // assignments.
        if text.is_empty() || !text.chars().all(|c| c.is_ascii_digit()) {
            trace!("Pollux input is empty or not all ASCII digits; skipping");
            return results;
        }

        // Low sensitivity is the convention for classical ciphers (see caesar_decoder
        // and railfence_decoder).
        let checker = checker.with_sensitivity(Sensitivity::Low);
        let morse = Decoder::<MorseCodeDecoder>::new();

        // Iterate every digit-to-class assignment as a base-3 counter over 10 digits.
        for assignment in 0u32..(3u32.pow(10)) {
            let morse_text = digits_to_morse(text, assignment);
            // MorseCodeDecoder drops an empty string without calling the checker, and
            // also drops a morse string that doesn't decode to anything. Either is a
            // miss for this assignment.
            let decoded = morse.crack(&morse_text, &checker);
            if decoded.success {
                results.success = true;
                results.unencrypted_text = decoded.unencrypted_text;
                results.checker_name = decoded.checker_name;
                results.checker_description = decoded.checker_description;
                results.key = Some(format_pollux_key(assignment));
                return results;
            }
        }

        // No assignment made the checker accept a reading. Returning every unread
        // decoding would explode the search graph, so leave unencrypted_text None.
        results
    }

    fn get_tags(&self) -> &Vec<&'static str> {
        &self.tags
    }
    fn get_name(&self) -> &str {
        self.name
    }
    fn get_popularity(&self) -> f32 {
        self.popularity
    }
    fn get_description(&self) -> &str {
        self.description
    }
    fn get_link(&self) -> &str {
        self.link
    }
}

/// Translate `text` (digits only) into Morse using the digit-to-class assignment
/// encoded as a base-3 number over 10 digits.
///
/// Digit `d` becomes the symbol of the class stored in bits `2*d` and `2*d+1` of
/// `assignment`.
fn digits_to_morse(text: &str, assignment: u32) -> String {
    let mut out = String::with_capacity(text.len());
    for c in text.chars() {
        let digit = (c as u8 - b'0') as u32;
        let class_bits = (assignment >> (2 * digit)) & 0b11;
        let class = match class_bits {
            0 => PolluxClass::Dot,
            1 => PolluxClass::Dash,
            _ => PolluxClass::Sep,
        };
        out.push(class.symbol());
    }
    out
}

/// Format the recovered digit-to-class assignment for the issue's example. The
/// canonical form groups the digits that map to each class and lists the classes in
/// `. - x` order, mirroring the issue's worked example: `. = 1 4 7, - = 2 5 8, x =
/// 3 6 9 0`.
fn format_pollux_key(assignment: u32) -> String {
    let mut dots = String::new();
    let mut dashes = String::new();
    let mut seps = String::new();
    for digit in 0u8..10 {
        let class_bits = (assignment >> (2 * digit as u32)) & 0b11;
        let target = match class_bits {
            0 => &mut dots,
            1 => &mut dashes,
            _ => &mut seps,
        };
        target.push((b'0' + digit) as char);
    }
    format!(". = {dots}, - = {dashes}, x = {seps}")
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::{
        checkers::{
            athena::Athena,
            checker_type::{Check, Checker},
            CheckerTypes,
        },
        decoders::interface::Crack,
    };

    fn get_athena_checker() -> CheckerTypes {
        let athena_checker = Checker::<Athena>::new();
        CheckerTypes::CheckAthena(athena_checker)
    }

    #[test]
    fn digits_to_morse_uses_issue_example_key() {
        // The issue's example: `. = 1 4 7, - = 2 5 8, x = 3 6 9 0`
        let assignment = build_assignment(
            &[1, 4, 7],    // dots
            &[2, 5, 8],    // dashes
            &[3, 6, 9, 0], // separators
        );
        // "HELLO" -> ".... . .-.. .-.. ---"
        assert_eq!(
            digits_to_morse("147414741147147147414741147147414714", assignment),
            ".... . .-.. .-.. ---"
        );
    }

    #[test]
    fn empty_text_is_not_a_success() {
        let decoder = Decoder::<PolluxDecoder>::new();
        let result = decoder.crack("", &get_athena_checker());
        assert!(!result.success);
    }

    #[test]
    fn non_digit_text_is_not_a_success() {
        let decoder = Decoder::<PolluxDecoder>::new();
        // The Pollux ciphertext is digits only. Anything else isn't Pollux.
        let result = decoder.crack("hello world", &get_athena_checker());
        assert!(!result.success, "Result: {:?}", result);
    }

    #[test]
    fn emoji_input_is_not_a_success() {
        let decoder = Decoder::<PolluxDecoder>::new();
        let result = decoder.crack("🦀🌍🐌", &get_athena_checker());
        assert!(!result.success);
    }

    #[test]
    fn issue_example_decodes() {
        // Issue #1000: 7774640754467514028890485358201240751738773 -> "HELLO WORLD"
        // key: . = 1 4 7, - = 2 5 8, x = 3 6 9 0
        let decoder = Decoder::<PolluxDecoder>::new();
        let result = decoder.crack(
            "7774640754467514028890485358201240751738773",
            &get_athena_checker(),
        );
        assert!(result.success, "Result: {:?}", result);
        let plaintext = &result.unencrypted_text.expect("no plaintext")[0];
        assert_eq!(plaintext, "HELLO WORLD");
        // The recovered key matches the issue's example.
        assert_eq!(result.key.as_deref(), Some(". = 147, - = 258, x = 3690"));
    }

    /// Build an assignment from three lists of digits. Used by tests.
    fn build_assignment(dots: &[u8], dashes: &[u8], seps: &[u8]) -> u32 {
        let mut assignment = 0u32;
        for &d in dots {
            assignment |= 0b00 << (2 * d as u32);
        }
        for &d in dashes {
            assignment |= 0b01 << (2 * d as u32);
        }
        for &d in seps {
            assignment |= 0b10 << (2 * d as u32);
        }
        assignment
    }
}
