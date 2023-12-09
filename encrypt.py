from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode('utf-8'))
    return cipher_text

def main():
    data_to_encrypt = input("Enter the data to encrypt: ")
    key = generate_key()
    encrypted_data = encrypt_data(key, data_to_encrypt)

    with open("encryption_key.txt", "w") as key_file:
        key_file.write(key.decode('utf-8'))

    with open("encrypted_data.txt", "wb") as data_file:
        data_file.write(encrypted_data)

if __name__ == "__main__":
    main()
