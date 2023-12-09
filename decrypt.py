from cryptography.fernet import Fernet

def decrypt_data(key, cipher_text):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode('utf-8')
    return plain_text

def main():

    with open('encryption_key.txt') as key_file:
        key = key_file.read().strip()
    with open('encrypted_data.txt', 'rb') as data_file:
        encrypted_data = data_file.read()

    decrypted_data = decrypt_data(key.encode('utf-8'), encrypted_data)
    print("Decrypted Data:", decrypted_data)

if __name__ == "__main__":
    main()
