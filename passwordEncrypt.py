from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode('utf-8'))
    return cipher_text

def decrypt_data(key, cipher_text):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode('utf-8')
    return plain_text

def main():
    # Generate a key (keep this secret and safe)
    key = generate_key()

    # Data to be encrypted
    original_data = "Hello, this is a secret message."

    # Encrypt the data
    encrypted_data = encrypt_data(key, original_data)
    print("Encrypted Data:", encrypted_data)

    # Decrypt the data
    decrypted_data = decrypt_data(key, encrypted_data)
    print("Decrypted Data:", decrypted_data)

if __name__ == "__main__":
    main()
