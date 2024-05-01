# Python Data Encryption

Simple Python3 project to encrypt and decrypt data using AES 128bit ( secret key 16 characters )

## Getting Started

### Installing

### macOS
* macOS - install homebrew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
* Get python3 on terminal
```
brew install python3
```
* Get pip3 on terminal
```
brew postinstall python3
```


* Get make sure you only have pycryptodome
```
pip3 uninstall pycrypto
```
```
pip3 uninstall pycryptodome
```
```
pip3 install pycryptodome
```

## How to Use
### Encrypt File

* Open the terminal on the project folder
* Edit the aes_secret_key.txt to your new secret key [you need it to decrypt the file]
* If aes_secret_key.txt not exist, the app will create a random 16 characters for the secret_key to [aes_secret_key_generated.txt]
```
python3 aes_encrypt.py
```
* Select a file to encrypt [selected file will be deleted!] ### WARNING ###
* Original file with ".encrypted" will be produced if encryption is successful

### Decrypt File

* Open the terminal on the project folder
* Edit the aes_secret_key.txt to your new secret key [you need it to decrypt the file]
```
python3 aes_decrypt.py
```
* Select a file to decrypt [selected file will be deleted!] ### WARNING ###
* Original file without ".encrypted" will be produced if encryption is successful


## Future Update

May make a GUI App for this

## Authors

Michael Hartomo

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
