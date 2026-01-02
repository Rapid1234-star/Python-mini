#Encryption Program
import random
import string

chars = " " +string.punctuation +string.digits + string.ascii_letters

chars=list(chars)
key=chars.copy()

random.shuffle(key)

#Encryption process
plain_txt=input("Enter a message to encrypt: ")
cipher_txt=""

for char in plain_txt:
    index=chars.index(char)
    cipher_txt+=key[index]

print(f"Original Message: {plain_txt}")
print(f"Encrypted Message: {cipher_txt}")

#Decryption process
decipher_txt=input("Enter a message to decrypt: ")
original_txt=""

for char in decipher_txt:
    index=key.index(char)
    original_txt+=chars[index]

print(f"Encrypted Message: {decipher_txt}")
print(f"Decrypted Message: {original_txt}")


