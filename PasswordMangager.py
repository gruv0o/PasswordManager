import sqlite3
import string
import secrets
import win32crypt
import bcrypt

from cryptography.fernet import Fernet


# Génération de clé de enfranchisement qui sera stockée
def generate_key():
    generated_key = Fernet.generate_key()

    with open('key.key', 'wb') as generated_key_file:
        generated_key_file.write(generated_key)


def encrypt_password(user_password):
    with open('key.key', 'rb') as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    encrypted_password = cipher_suite.encrypt(user_password.encode())

    return encrypted_password

# Chiffrement d'un mot de passe choisi par l'utilisateur
def decrypt_password(user_encrypted_password):
    with open('key.key', 'rb') as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    decrypted_password = cipher_suite.decrypt(user_encrypted_password).decode()

    return decrypted_password

generate_key()
print("Bonjour! Nous allons chiffrer votre mot de passe et voir ce que ça donne..")
user_password = input("\nVeuillez entrer votre mot de passe: ")

decrypted_password = encrypt_password(user_password)
print("Voici votre mot de passe chiffré:\n")
print(decrypted_password)

# création et chiffrement d'un mot de passe généré
# création, hashage et stockage du master password
# stockage des mot de passe chiffré
# lecture et déchiffrement
