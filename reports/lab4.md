# Hash functions and Digital Signatures

## Course: Cryptography & Security

### FAF - 203

### Author: Ana Corolețchi

----

## Theory

### What is hashing?

A __hash value__ is the output of plaintext or ciphertext. __Hashing__ is a cryptographic technique that transforms any form of data into a special text string. For any given input, there is a deterministic output. When you put a plaintext into a hashing algorithm in simpler terms, you get the same outcome. Suppose you change anything about the input or the plaintext to the hashing algorithm. The hashing output also becomes different.

### How hashing works?

Hashing works by converting a readable text into an unreadable text of secure data. Hashing is efficiently executed but extremely difficult to reverse. Like I stated earlier, hashing and encryption are often mistaken. Encryption is a two-way function. The plaintext can be encrypted into ciphertext and decrypted back into plaintext using a unique key. The difference between encryption and hashing is that encryption is reversible while hashing is irreversible.

Hashing takes the password a user enters and randomly generates a hash using many variables (text and numbers). When you input your password to log in, it is matched to the hash password. This is because the input is the same as the output.

For example: In the bank, when you apply for a credit card. You create a password to help you access your account. The bank system does not save your password. The bank system runs the password through a hashing algorithm. It then saves the hash as your password. Every time you attempt to log in to your account. The bank system compares the password you enter with the hash it has saved. Only when the two-match, do you get authorization to access your bank account.

Hashing enables people to get data authorization without knowing the content on the data. We use hashing algorithms and databases to store passwords. Passwords are saved in the form of a hash value or a hash password rather than as plaintext. The hash value makes the data more secure.

Cryptographic hashing provides a barrier to potential attackers. In case a malicious person tries accessing the database, the person can see the hashes. However, the attacker cannot reverse the hash value back to the actual password.

The purpose of hashing is:

1. To verify data integrity.
2. Authentication.
3. To store sensitive data.

### Types of hashing algorithms

__Message digest 5 (MD5).__ Message digest 5 (MD5) is a one-way cryptographic hash algorithm. It generates a 128-bit string value as the hash value or the digest. MD5 is often used to verify data integrity.

__Secure hashing algorithm 1 (SHA1).__ This is a cryptographic hash algorithm, that generates a 160-bit string value as the hash value. This hashing algorithm was developed by the National Security Agency (NSA). SHA1 is commonly used in security and data integrity applications.

__Secure hashing algorithm 256 (SHA256).__ This is a cryptographic hash algorithm that creates a 256-bit (32 bytes) string value as the hash value. SHA256 often checks the data integrity for hash authentication and digital signatures.

### Applications of hashing

__Password storage.__ Hashing protects how passwords are stored and saved. Instead of keeping a password, in the form of a plaintext. It is stored as a hash value or a digest. The hash values are stored in a hash table.An intruder can only see the hash values and cannot log into a system using the hash value.

__Password verification.__ Hashing is used for password verification every time you login into an application, account, or system. A password verifies if you are the actual user of that account. If the password you enter matches the hash value on the server-side, you get authorization.

__Checking of data integrity.__ Hashing checks for data integrity. It gives the user assurance that no data has been modified and the data is correct. It also assures the user that the data is original.

### Digital Signature

A __digital signature__ is a mathematical technique used to validate the authenticity and integrity of a message, software, or digital document. Digital Signature in Cryptography is a value calculated from the data along with a secret key that only the signer is aware of. The receiver needs to be assured that the message belongs to the sender. This is crucial in businesses as the chances of disputes over data exchange are high. There are three algorithms at work in Digital Signatures. They are as follows:

1. __Key Generation Algorithms :__ Digital signature is electronic signatures, which assure that the message was sent by a particular sender. While performing digital transactions authenticity and integrity should be assured, otherwise, the data can be altered or someone can also act as if he was the sender and expect a reply.
2. __Signing Algorithms :__ To create a digital signature, signing algorithms like email programs create a one-way hash of the electronic data which is to be signed. The signing algorithm then encrypts the hash value using the private key (signature key). This encrypted hash along with other information like the hashing algorithm is the digital signature. This digital signature is appended with the data and sent to the verifier. The reason for encrypting the hash instead of the entire message or document is that a hash function converts any arbitrary input into a much shorter fixed-length value. This saves time as now instead of signing a long message a shorter hash value has to be signed and moreover hashing is much faster than signing.
3. __Signature Verification Algorithms :__ Verifier receives Digital Signature along with the data. It then uses Verification algorithm to process on the digital signature and the public key (verification key) and generates some value. It also applies the same hash function on the received data and generates a hash value. Then the hash value and the output of the verification algorithm are compared. If they both are equal, then the digital signature is valid else it is invalid.

The steps followed in creating digital signature are :

1. Message digest is computed by applying hash function on the message and then message digest is encrypted using private key of sender to form the digital signature. (digital signature = encryption (private key of sender, message digest) and message digest = message digest algorithm(message)).
2. Digital signature is then transmitted with the message.(message + digital signature is transmitted)
3. Receiver decrypts the digital signature using the public key of sender.(This assures authenticity, as only sender has his private key so only sender can encrypt using his private key which can thus be decrypted by sender’s public key).
4. The receiver now has the message digest.
5. The receiver can compute the message digest from the message (actual message is sent with the digital signature).
6. The message digest computed by receiver and the message digest (got by decryption on digital signature) need to be same for ensuring integrity.
7. Message digest is computed using one-way hash function, i.e. a hash function in which computation of hash value of a message is easy but computation of the message from hash value of the message is very difficult.

## Objectives

1. Get familiar with the hashing techniques/algorithms.
2. Use an appropriate hashing algorithms to store passwords in a local DB.
    1. You can use already implemented algortihms from libraries provided for your language.
    2. The DB choise is up to you, but it can be something simple, like an in memory one.
3. Use an asymmetric cipher to implement a digital signature process for a user message.
    1. Take the user input message.
    2. Preprocess the message, if needed.
    3. Get a digest of it via hashing.
    4. Encrypt it with the chosen cipher.
    5. Perform a digital signature check by comparing the hash of the message with the decrypted one.

## Implementation description

At this laboratory work, the user need to enter his credential : username and password. Then, the password will be hashed using `haslib` library from Python.
In `haslib`, there is one constructor method named for each type of hash. All return a hash object with the same simple interface. For example, I used `sha256()` to create a SHA-256 hash object. You can now feed this object with bytes-like objects (normally bytes) using the `update()` method. At any point you can ask it for the digest of the concatenation of the data fed to it so far using the `digest()` or `hexdigest()` methods.
Assymetric encryption was done using `RSA` algorithm. Also, ther is another library for it, called `cryptography` which is responsible of `hashes` module.

</br>

### Asymmetric encryption and decryption

```python
@staticmethod
    def assymetric_encryption(msg):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        public_key = private_key.public_key()

        encrypted = public_key.encrypt(
            msg,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return encrypted, private_key

@staticmethod
    def assymetric_decryption(encrypted_message, private_key):
        original_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return original_message
```

### Digital signature check

```python
@staticmethod
    def digital_signature_check(original_message, decrypted_message):
        if sha256(original_message.encode()).hexdigest() == decrypted_message:
            print("Success! Hashes are the same")
```

### Main function

```python

if __name__ == '__main__':
    
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Get a digest of it via hashing
    hashed_password = sha256(password.encode()).hexdigest()
    print("The hashed password is: ", hashed_password)

    # Encrypted message.
    encrypted_message, private_key = DigitalSignature.assymetric_encryption(
        hashed_password.encode())
    print("Encrypted message is: ", encrypted_message)
    
    # Decrypted message.
    decrypted_message = DigitalSignature.assymetric_decryption(
        encrypted_message, private_key).decode()
    print("Decrypted message is: ", decrypted_message)
    
    # Perform a digital signature check by comparing the hash of the message with the decrypted one.
    DigitalSignature.digital_signature_check(password, decrypted_message)
```

The output of my code will be :

```txt
Enter a username: ana07
Enter a password: 12345678
The hashed password is:  ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f
Encrypted message is:  b'_zh\xfaU\x0e-\x04ajtw6y\xdaW\xae\xe4\xaa\x04-qw\x99\xa2\xe7\x0e\x8dK\xac\x90\x06\xb1\xfa\n\xd4\x84\tV\xcb\x9c\xd8w\x04y=\xfc#\xfd\xd0\xef\x00\x92\xc6B:\x91B\xe0d%]7\x95~\xf7\xaf\xf2ku\xaf\xf7$\xce\x8f\x05\xba\x1a\xd6\x0c\x1dk\xec\x10\x01"\xa6\xab\xccsI?\xc7\x8e\x7f\xc3\x02\xde\xdd\xa9\x15\xb4f\x9d\x15\xda\xbe\xf7(z\xdb[\xf0\xdb0\x061"\x02e\xde\xd3%=d\xe0\'\xce\xbb42\xb65\xe4\xe4\x15\r_\xa4\xe7\xdcYM\xb0\xcb\x8e\x08\xa6\xc3\x0b\xa3v\x04\xdd\xb3\x9a5_\xaev5\xad`\x03;]\x94\t\xc54X\xeeI\x96\xb2)\xfd\x9bN\x8a\xcc;\xd2\xd2i\xb7\xab\xc3\x8f\xd7\x14\x87\xa1%\x05\x1aH"\xc7a\xa2\x04\xe0c\xa8\xffb\xb9\xcc:\xe9\xa1\xf7\xc2\x92Y^\n\t4]\xbf+\xa2\xa3f\x08\xd5\xedP\x8e\xd2i^\xd0E\x08\xcb\x1f\xc2+\xe2+\xb5y\x17\xe7\xa77\xdf\nd\xf0&J?'
Decrypted message is:  ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f
Success! Hashes are the same
```

</br>

## Conclusions

At this laboratoty work I found out how asymmetric ciphers are related to hashing, what is a digital signature check and how to hash a password, then encrypt it & decrypt and the to check if the initial hash with the final are the same.
Hashing and digital signatures are used nowadays, so it's kinda useful to know about them.
