Binoculars logo
# Ciphey (centered)
Automated Decryption Tool

# What is this?
Ciphey is an automated decryption tool. Input encrypted text, get the decrypted text back.
> "What time of encryption?"
That's the point. You don't know, you just know it's possibly encrypted. Ciphey will figure it out for you.

Ciphey uses a deep neural network to guess what something is encrypted with, and then a custom built natural language processing module to determine the output.

Ciphey can solve most things in under 3 seconds.
# Features
* Ciphey supports over 20 kinds of encryptions, such as hashes, encodings (binary, base64) and normal encryptions like Caesar cipher, Transposition and more. For the full list, check this out (LINK HERE)
* Ciphey's deep neural network helps it target the right encryption method the first time around, resulting in decryptions taking less than 3 seconds. If Ciphey cannot decrypt the text, Ciphey will use the neural network analysis to give you information on how to decrypt it yourself.
* The custom built natural language processing module is designed to be fast and accurcate. Ciphey can determine whether something likely isn't Engllish in a fraction of second, and it can determine for sure if something is English in < 0.5 seconds.
* Ciphey can support multiple languages (at present, only English.)
* Supports hashes & encryption methods, which the alternatives such as CyberChef do not. Also, it is physically quicker to pipe in data to Ciphey than it is to copy and paste it into a website with bloated JavaScript.
MAYBE TOO MANY FEATURES???
# Getting Started
## Installation
### Pip
```pip3 install ciphey```
```ciphey -t "encrypted text here"```
To run ciphey.

### Cloning from GitHub
```git clone https://github.com/brandonskerritt/ciphey```
cd ciphey && python3 ciphey -t "encrypted text here"```
To run ciphey
### Running Ciphey
To get rid of the progress bars, probability table, and all the noise use the grep mode.
```ciphey -t "encrypted text here" -g```
For a full list of arguments, run `ciphey -h`.

### FAQ
MAKE THIS COLLAPSABLE

Curious about the neural network or language checker? Read /docs
The Internal Data Packet

# Contributors
## Contributing
Please read the contributing file.
## Code Contributors
None
## Financial Contributors

<a target="_blank" href="https://icons8.com/icons/set/binoculars">iOS</a>, <a target="_blank" href="https://icons8.com/icons/set/binoculars">iOS Filled</a> and other icons by <a target="_blank" href="https://icons8.com">Icons8</a>


