# Symmetric Ciphers. Stream Ciphers. Block Ciphers

## Course: Cryptography & Security

### FAF - 203

### Author: Ana Corolețchi

----

## Theory

**Symmetric encryption** algorithms are categorized into two: block and stream ciphers. **Block ciphers** encrypt data in blocks of set lengths, while stream ciphers do not and instead encrypt plaintext one byte at a time. **Block ciphers** convert data in plaintext into ciphertext in fixed-size blocks. A **stream cipher** encrypts a continuous string of binary digits by applying time-varying transformations on plaintext data.

## Objectives

1. Get familiar with the symmetric cryptography, stream and block ciphers.

2. Implement an example of a stream cipher.

3. Implement an example of a block cipher.

4. The implementation should, ideally follow the abstraction/contract/interface used in the previous laboratory work.

5. Please use packages/directories to logically split the files that you will have.

6. As in the previous task, please use a client class or test classes to showcase the execution of your programs.

## Implementation description

I implemented DES Cipher and Rivest Cipher in Python. I used functions and sructured the code as it needed.
</br>

### Data Encryption Standard (DES)

A 56-bit symmetric key algorithm was initially used to protect sensitive, confidential information. DES has since been withdrawn due to short key length and other security concerns but is still viewed as a pioneer encryption standard.

```python
def DES(text, key, padding, isEncrypt):
    # Function to implement DES Algorithm.

    # Initializing variables required
    isDecrypt = not isEncrypt
    # Generating keys
    keys = generateKeys(key)

    # Splitting text into 8 byte blocks
    plaintext8byteBlocks = nSplit(text, 8)
    result = []

    # For all 8-byte blocks of text
    for block in plaintext8byteBlocks:

        # Convert the block into bit array
        block = stringToBitArray(block)

        # Do the initial permutation
        block = permutation(block, initialPermutationMatrix)

        # Splitting block into two 4 byte (32 bit) sized blocks
        leftBlock, rightBlock = nSplit(block, 32)

        temp = None

        # Running 16 identical DES Rounds for each block of text
        for i in range(16):
            # Expand rightBlock to match round key size(48-bit)
            expandedRightBlock = expand(rightBlock, expandMatrix)

            # Xor right block with appropriate key
            if isEncrypt == True:
                # For encryption, starting from first key in normal order
                temp = xor(keys[i], expandedRightBlock)
            elif isDecrypt == True:
                # For decryption, starting from last key in reverse order
                temp = xor(keys[15 - i], expandedRightBlock)
            # Sbox substitution Step
            temp = SboxSubstitution(temp)
            # Permutation Step
            temp = permutation(temp, eachRoundPermutationMatrix)
            # XOR Step with leftBlock
            temp = xor(leftBlock, temp)

            # Blocks swapping
            leftBlock = rightBlock
            rightBlock = temp

        # Final permutation then appending result
        result += permutation(rightBlock + leftBlock, finalPermutationMatrix)

    # Converting bit array to string
    finalResult = bitArrayToString(result)

    return finalResult
```

</br>

### Rivest Cipher (RC4)

**RC4/ARC4/ARCFOUR** is a fast, simple encryption algorithm developed in 1987 to implement byte-by-byte encryption using 64 or 128 bits long keys. RC4 is widely used in Transport Layer Security, Secure Sockets Layer, and the IEEE 802.11 WLAN standard. The popular encryption scheme comes in various flavors, including SPRITZ, RC4A, and RC4A+, among others.

```python
def KSA(key):
    # Key Scheduling Algorithm (from wikipedia):
    key_length = len(key)
    # create the array "S"
    S = list(range(MOD))  # [0,1,2, ... , 255]
    j = 0
    for i in range(MOD):
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i]  # swap values

    return S


def PRGA(S):
    # Pseudo Random Generation Algorithm
    i = 0
    j = 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % MOD]
        yield K
```

</br>

## Conclusions

At this laboratoty work I found out about stream and block ciphers. From all of them , I choose to implement Rivest Cipher and Data Encryption Standart Cipher.
