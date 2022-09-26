# Intro to Cryptography. Classical ciphers

## Course: Cryptography & Security

### FAF - 203

### Author: Ana Corolețchi

----

## Theory

**Classical ciphers** are ciphers developed prior to the invention of the computer. These are opposed to mechanical or modern ciphers, which require either machines or computers to decipher respectively.

**Classical ciphers** were used throughout all of history, up until the early days of World War II. They range in complexity from very simple to very complex. Similarly, some have been used by governments and militaries, while others have only ever been used by amateurs for entertainment.

Nowadays, the only reason to use a **classical cipher** is for entertainment. Even an old, slow computer can break any of these with relative ease. If you need real security, you’ll want to use a modern encryption method.

## Objectives

1. Get familiar with the basics of cryptography and classical ciphers.

2. Implement 4 types of the classical ciphers:
    - Caesar Cipher with one key used for substitution
    - Caesar Cipher with one key used for substitution, and a permutation of the alphabet
    - Vigenere Cipher
    - Playfair Cipher
    - Affine Cipher

## Implementation description

For every folder which contains the cipher, you can find the input `input.txt`, so the input will be genereat from the file. Same with the output, it will be generated in the `outputFile.txt`. The decrypted message, which must be the same as the original one, u'll find in the `checkDecrypt.txt` file. Implementation was written in **Python**.
</br>

### Affine Cipher

**Affine Cipher** is a simple substitution cipher.

```python
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
```

</br>

### The Caesar Cipher

**The Caesar Cipher** is a simple substitution cipher, where a letter is shifted either left or right by a certain number of positions in the alphabet. So with a left shift three, D would become A, E would become E, and so on.

```python
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
```

</br>

### Playfair Cipher

**Playfair Cipher** is a substitution cipher, but it uses pairs of letters instead of single letters to represent a single ciphertext character. Because it uses pairs of characters, frequency analysis code-breaking techniques are ineffective.

```python
def encrypt(self, msg):
        pairs = PlayfairCipher.prepare(msg)
        return ' '.join(self.transform(pair, 1) for pair in pairs)

def decrypt(self, msg):
    msg = msg.upper()
    PlayfairCipher.check_input(msg)
    if not re.match(r'^([A-Z]{2}(\s)?)+$', msg):
        raise ValueError(
            "The inputted message isn't a valid Playfair cipher message")
    msg = re.findall('[A-Z]{2}', msg)
    def rule1(x): return x if x[1] != 'X' else x[0]
    return ' '.join(rule1(self.transform(s, -1)) for s in msg)

```

</br>

### Vigenere Cipher

**Vigenère Cipher** is a polyalphabetic substitution cipher. Virtually impossible to decipher without a code book or a computer.

```python
def encrypt(message, key):
    encrypted = ""
    split_message = [
        message[i: i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] +
                      letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i: i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] -
                      letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted
```

</br>

## Conclusions

For this laboratory work I found out how the ciphers work. Even if they are old and not used today, they are the basis of the modern cryptohgraphy. For me, the Playfair Cipher was the most hard to implement. On the other hand, the Caesar Cipher was the easiest one to implement.
