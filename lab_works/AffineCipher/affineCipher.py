def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


class AffineCipher:

    def encrypt(self, text, k, p):
        encryptedString = ""
        for t in text.upper():
            if(t.isalpha()):
                encryptedString += chr(((k*(ord(t) - ord('A')) + p) %
                                       26) + ord('a'))
            else:
                encryptedString += t
        return encryptedString

    def decrypt(self, cipher, k, p):
        decryptedString = ""
        for c in cipher:
            if(c.isalpha()):
                decryptedString += chr(((modinv(k, 26)*(ord(c) - ord('a') - p))
                                        % 26) + ord('a'))
            else:
                decryptedString += c
        return decryptedString


class writeFile:
    def writeFile(self, fileName, content):
        f = open(fileName, 'w')
        f.write(content)
        f.close()


file = writeFile()
cipher = AffineCipher()

with open('lab1/AffineCipher/input.txt') as text:
    text = text.read()

istring = cipher.encrypt(text, 1, 3)

# writing output to a file
file.writeFile("outputFile.txt", istring)

# checking the decrypt function
dstring = cipher.decrypt(istring, 1, 3)
file.writeFile('checkDecrypt.txt', dstring)
