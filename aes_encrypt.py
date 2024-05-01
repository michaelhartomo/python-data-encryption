import sys
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.withdraw()

# file_data = filedialog.askopenfilename()
file_data = "file_test/avatar.jpg"
file_secret_key = "aes_secret_key.txt"

# Check if file exist, if not exit
if os.path.isfile(file_data):
    with open(file_data, "rb") as f:
        data_original = f.read()
else:
    print("[file_data] not found!")
    sys.exit()


# Check if file exist, if not exit
if os.path.isfile(file_secret_key):
    with open(file_secret_key, "rb") as f:
        secret_key = f.read()
else:
    # Generate random secret key
    secret_key = get_random_bytes(16)
    with open("aes_secret_key_generated.txt", "wb") as f:
        f.write(secret_key)


if len(secret_key) > 16:
    secret_key = secret_key[0:16]
elif len(secret_key) < 16:
    secret_key = secret_key.ljust(16)

cipher = AES.new(secret_key, AES.MODE_OCB)
ciphertext, tag = cipher.encrypt_and_digest(data_original)
assert len(cipher.nonce) == 15

with open(file_data+".encypted", "wb") as f:
    f.write(tag)
    f.write(cipher.nonce)
    f.write(ciphertext)
    # remove original data
    os.remove(file_data)

print("encryption is complete")