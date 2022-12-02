from hashlib import sha256
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

database = {}

class DigitalSignature:

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

    @staticmethod
    def digital_signature_check(original_message, decrypted_message):
        if sha256(original_message.encode()).hexdigest() == decrypted_message:
            print("Success! Hashes are the same")

    @staticmethod
    def save_to_datastore(key, input_string):
        database[key] = sha256(input_string).hash


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