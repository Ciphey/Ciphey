plain = input("Enter plaintext: ").strip().upper()
plain = filter(lambda x: x.isalpha() or x == " ", plain)
key = input("Enter key: ").strip().replace("-", "").upper()
i = 0
ciphertext = ""
for char in plain:
    if char != " ":
        ciphertext += chr(
            (((ord(char) - 65) + (ord(key[i]) - 65)) % 26) + 65
        )  # ^Find the number corresponding to each letter, add them together, mod26, then convert back to a letter.
        i += 1
    else:
        ciphertext += " "

print(ciphertext)

output = ""
i = 0
for char in ciphertext:
    if char != " ":
        output += chr((((ord(char) - 65) - (ord(key[i]) - 65)) % 26) + 65)
        i += 1
    else:
        output += " "

print(output)

# ( ͡° ͜ʖ ͡°)
