import sys
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_data_encrypted = filedialog.askopenfilename()
# file_data_encrypted = "file_test/avatar.jpg.encrypted"
file_secret_key = "aes_secret_key.txt"


# Check if file exist, if not exit
if os.path.isfile(file_secret_key):
    file_secret_key_checked = file_secret_key
elif os.path.isfile("aes_secret_key_generated.txt"):
    file_secret_key_checked = "aes_secret_key_generated.txt"
else:
    print("[secret_key] not found!")
    sys.exit()


with open(file_secret_key_checked, "rb") as f:
    secret_key = f.read()
    # check secret_key length
    if len(secret_key) > 16:
        secret_key = secret_key[0:16]
    elif len(secret_key) < 16:
        secret_key = secret_key.ljust(16)

# decryption test
# Check if file exist, if not exit
if os.path.isfile(file_data_encrypted):
   with open(file_data_encrypted, "rb") as f:
    tag = f.read(16)
    nonce = f.read(15)
    data_encrypt = f.read()
else:
    print("[file_data_encrypted] not found!")
    sys.exit()

cipher = AES.new(secret_key, AES.MODE_OCB, nonce)
try:
    data_decrypt = cipher.decrypt_and_verify(data_encrypt, tag)
    filename_original = file_data_encrypted[0:len(file_data_encrypted)-9]
    with open(filename_original, "wb") as f:
        f.write(data_decrypt)
        # remove encrypted data
        os.remove(file_data_encrypted)
except ValueError:
    print("The [encrypted_data] or [secret_key] was modified!")
    sys.exit(1)