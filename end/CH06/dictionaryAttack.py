#!/usr/bin/env python3
# Script that performs a dictionary attack 
# against known password hashes
# Needs a dictionary file to run. Suggested to use 
# https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Christy Willingham
# date: 7/30/25

# Import necessary Python modules
import os
import sys
from passlib.hash import sha512_crypt

def test_password(hashed_password, 
    salt, plaintext_password):
        crypted_password = sha512_crypt.using(rounds=5000).hash(
        plaintext_password, salt=salt)
        if hashed_password == crypted_password:
         return True
        return False
    
def read_dictionary(dictionary_file):
    file_path = os.path.join(script_dir, dictionary_file)
    f = open(file_path, "r")
    message = f.read()
    return message

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

password_dictionary = read_dictionary("top1000.txt")
hashed_password = input("What is the hashed password? ")
hash_parts = hashed_password.split("$")
salt = hash_parts[2]

for password in password_dictionary.splitlines():
    result = test_password(hashed_password, salt, password)
    if result:
        print("Match found: {0}".format(password))
        sys.exit()
print("No match found, try a different dictionary")
