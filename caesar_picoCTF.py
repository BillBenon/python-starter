def decryptor(key, ciphertext):
    plaintext = ""
    for c in ciphertext:
        newChar = ord(c) - key
        if newChar < ord("a"):
            newChar = newChar + 26
        plaintext += chr(newChar)
    return plaintext


ciphertext = "dspttjohuifsvcjdpoabrkttds"
# For each valid key value
for i in range(1, 26):
    plaintext = decryptor(i, ciphertext)
    print("key is: ", i, "text is: ", plaintext)
