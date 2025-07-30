#!/usr/bin/env python3
# Script that hashes a password
# By Christy Willingham
# date: 7/30/2025

import crypt
print(crypt.crypt("qwerty"))
print(crypt.crypt("qwerty", "$6$DQbbDT6LL08XasAC9$"))