#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Christy Wilingham
import hashlib
import requests

def sha1_hash(text):
    hash_object = hashlib.sha1()
    bytes_text = text.encode()
    hash_object.update(bytes_text)
    hex_dig = hash_object.hexdigest()
    return hex_dig.upper()
def check_haveibeenpwned(sha_prefix):
    url = "https://api.pwnedpasswords.com/range/" +sha_prefix
    payload={}
    headers={}
    response = requests.request("GET" , url, headers=headers, data=payload)
    pwnd_list = response.text.split("\r\n")
    pwnd_dict = {}
    for pwnd_resp in pwnd_list:
        tmp_hash=pwnd_resp.split(":")
        pwnd_dict[tmp_hash[0]] = tmp_hash[1]
    return pwnd_dict

password = input("What is the password to check? ")
sha_password = sha1_hash(password)
sha_prefix = sha_password[0:5]
sha_postfix = sha_password[5:]
pwnd_dict = check_haveibeenpwned(sha_prefix)
if sha_postfix in pwnd_dict.keys():
    print("This password has been compromised {0} times".format(pwnd_dict[sha_postfix]))
else:
    print("This password is secure!!")