from cryptography.fernet import Fernet
from glob import glob
import sys
import os

def write_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def read_key():
    return open("secret.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        
    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        
    decrypted_data = f.decrypt(file_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

if not "secret.key" in os.listdir():
    write_key()

key = read_key()

if sys.argv[1] == "encrypt":
    files_to_encrypt = glob("./important data/*")
    for file in files_to_encrypt:
        encrypt(file, key)

elif sys.argv[1] == "decrypt":
    files_to_decrypt = glob("./important data/*")
    for file in files_to_decrypt:
        decrypt(file, key)
