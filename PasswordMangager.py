import sqlite3
import string
import secrets
import win32crypt
import bcrypt

from cryptography.fernet import Fernet

#Génération de clé de chiffrement qui sera stocké
def Generate_key():
    key = Fernet.generate_key()

    with open('key.key', 'wb') as key_file:
        key_file.write(key)

Generate_key()

#Chiffrement d'un mot de passe choisi par l'utilisateur
#création et chiffrement d'un mot de passe généré
#création, hashage et stockage du master password
#stockage des mot de passe chiffré
#lecture et déchiffrement

