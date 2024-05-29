import sqlite3
import string
import secrets
import win32crypt
from cryptography.fernet import Fernet

#Génération de clé de chiffrement qui sera stocké
#Chiffrement d'un mot de passe choisi par l'utilisateur
#création et chiffrement d'un mot de passe généré
#création, hashage et stockage du master password
#stockage des mot de passe chiffré
#lecture et déchiffrement

