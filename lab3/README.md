# Asymmetric Ciphers. RSA

## Course: Cryptography & Security

### FAF - 203

### Author: Ana Corolețchi

----

## Theory

__Asymmetric key cryptosystems__ / __public-key cryptosystems__ (like RSA, elliptic curve cryptography (ECC), Diffie-Hellman, ElGamal, McEliece, NTRU and others) use a pair of mathematically linked keys: __public key (encryption key)__ and __private key (decryption key)__.

The asymmetric key cryptosystems provide key-pair generation (__private + public key__), encryption algorithms (asymmetric key ciphers and encryption schemes like RSA-OAEP and ECIES), digital signature algorithms (like DSA, ECDSA and EdDSA) and key exchange algorithms (like DHKE and ECDH).

A message encrypted by the __public key__ is later decrypted by the __private key__. A message signed by the private key is later verified by the public key. The public key is typically shared with everyone, while the private key is kept secret. Calculating the private key from its corresponding public key is by design computationally infeasible.

## Objectives

1. Get familiar with the asymmetric cryptography mechanisms.

2. Implement an example of an asymmetric cipher.

3. As in the previous task, please use a client class or test classes to showcase the execution of your programs.

## Implementation description

I implemented RSA Cipher in Python. I used functions and sructured the code as it needed.
</br>

### RSA

The __RSA__ algorithm is named after Ron Rivest, Adi Shamir and Len Adleman, who invented it in 1977 [RIVE78]. The basic technique was first discovered in 1973 by Clifford Cocks [COCK73] of CESG (part of the British GCHQ) but this was a secret until 1997. The patent taken out by RSA Labs has expired.

The RSA cryptosystem is the most widely-used public key cryptography algorithm in the world. It can be used to encrypt a message without the need to exchange a secret key separately.

The RSA algorithm can be used for both public key encryption and digital signatures. Its security is based on the difficulty of factoring large integers.

Party A can send an encrypted message to party B without any prior exchange of secret keys. A just uses B's public key to encrypt the message and B decrypts it using the private key, which only he knows. RSA can also be used to sign a message, so A can sign a message using their private key and B can verify it using A's public key.

Function to generate keys

```python

def generate_keypair(p, q, f, n):
    # choose an integer e such that e and f(n) are coprime
    e = random.randrange(2, f)
    # verify that e and f(n) are comprime
    g = gcd(e, f)
    while g != 1:
        e = random.randrange(2, f)
        g = gcd(e, f)

    # use Extended Euclid's Algorithm to generate the private key
    d = modular_inverse(e, f)

    # return public and private keypair
    return ((e, n), (d, n))
```

Function to check if they are prime

```python
def isPrime(i):
    for j in range(2, i):
        if(i % j == 0):
            return False
    return True


# function to calcuate gcd
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```

Function to calculate inverse of e using Extended Eculidean Method

```python
def modular_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0

    return x
```

Encryption and decryption

```python
def encrypt(publicKey, message):
    e, n = publicKey
    # converts each letter in the plaintext to numbers based on the character using a^b mod m
    c = [(ord(char) ** e) % n for char in message]

    return c

def decrypt(privateKey, message):
    d, n = privateKey
    # generates the plaintext based on the ciphertext and key using a^b mod m
    p = [chr((char ** d) % n) for char in message]
    # Return the array
    return ''.join(p)
```

The output of my code will be :

```
Enter the value of prime number p = 11
Enter the value of prime number q = 13
Enter the message m = anisoara
Public Key [e,n] =  (101, 143)
Cipher text =  [119, 132, 105, 137, 89, 119, 4, 119]
Private Key [d,n] =  (101, 143)
Plain text after decryption =  anisoara
```

</br>

## Conclusions

At this laboratoty work I found out asymmetric ciphers and choose to implement RSA Cipher. This cipher requires knowlege of prime and coprime numbers, Euler's totient function, GCD and modular multiplicative inverse.