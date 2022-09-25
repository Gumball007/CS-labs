class CaesarCipher:

    def encrypt(self, text, step):
        encryptedString = ""
        for t in text.upper():
            if(t.isalpha()):
                encryptedString += chr(ord('a') +
                                       ((ord(t) + step - ord('A')) % 26))
            else:
                encryptedString += t
        return encryptedString

    def decrypt(self, cipher,  step):
        decryptedString = ""
        for c in cipher:
            if(c.isalpha()):
                decryptedString += chr(ord('a') +
                                       ((ord(c) - step - ord('a')) % 26))
            else:
                decryptedString += c
        return decryptedString


class writeFile:
    def writeFile(self, fileName, content):
        f = open(fileName, 'w')
        f.write(content)
        f.close()


file = writeFile()
cipher = CaesarCipher()

with open('lab1/CaesarCipher/input.txt') as text:
    text = text.read()

# encrypting input with caesar cipher
istring = cipher.encrypt(text, 5)

# writing output to a file
file.writeFile("outputFile.txt", istring)

# checking the decrypt function
dstring = cipher.decrypt(istring, 5)
file.writeFile('checkDecrypt.txt', dstring)
