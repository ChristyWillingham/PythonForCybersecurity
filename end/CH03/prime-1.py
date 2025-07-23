# !/usr/bin/env python3
# example prime numbers
# By Christy Willingham

from math import sqrt

def check_prime(number):
    if number < 2:
        return False
    
    limit = int(sqrt(number)) + 1 
    for index in range(2, limit):
        if number % index == 0:
            return False
        
    return True

n = int(input("What is your favorite number : "))
if check_prime(n):
    print("Number is a Prime Number")
else:
    print("Number is not a Prime Number")

        