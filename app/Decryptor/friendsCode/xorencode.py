plain = input("Enter plaintext: ").strip()
key = input("Enter key: ").strip()

i = 0
ciphertext = ""
for char in plain:
    if char != " ":
        ciphertext += chr((ord(char)) ^ (ord(key[i])))
        i += 1
    else:
        ciphertext += " "

print("Ciphertext (basically useless):\n" + ciphertext)

print("Ascii Values:")
for x in ciphertext:
    if x != " ":
        val = ord(x)
        print(val, end=" ")
        print("In binary: {0:b}".format(val))

# ( ͡° ͜ʖ ͡°)
