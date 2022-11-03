import random

# function to generate keys
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


# function to check prime
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


# function to calculate inverse of e using Extended Eculidean Method
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

# encryption & decryption : cipher text c = m^e mod n ; plain text d= c^d mod n
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


# validates if entered p,q are prime 
while True:
    try:
        p = int(input('Enter the value of prime number p = '))
    except ValueError:
        print("InValid Input")
        continue
    if not isPrime(p):
        print("Enter a prime number")
        continue
    else:
        break
while True:
    try:
        q = int(input('Enter the value of prime number q = '))
    except ValueError:
        print("InValid Input")
        continue
    if not isPrime(q):
        print("Enter a prime number")
        continue
    else:
        break


n = p * q
# calculates f(n) 
f = (p - 1) * (q - 1)
publicKey, privateKey = generate_keypair(p, q, f, n)

m = input('Enter the message m = ')
print('Public Key [e,n] = ', publicKey)

# Encrypt
c = encrypt(publicKey, m)
# Decrypt
m = decrypt(privateKey, c)

print('Cipher text = ', c)
print('Private Key [d,n] = ', privateKey)
print('Plain text after decryption = ', m)
