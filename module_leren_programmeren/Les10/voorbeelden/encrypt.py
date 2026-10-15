from cryptography.fernet import Fernet

# 1. Generate a secure 32-byte URL-safe base64 key
key = Fernet.generate_key()

# 2. Initialize the Fernet cipher suite
cipher_suite = Fernet(key)

# 3. Encrypt a message (must be bytes)
message = b"my deep dark secret"
encrypted_token = cipher_suite.encrypt(message)
print("Encrypted:", encrypted_token)

# 4. Decrypt the message back to plaintext
decrypted_message = cipher_suite.decrypt(encrypted_token)
print("Decrypted:", decrypted_message.decode())
