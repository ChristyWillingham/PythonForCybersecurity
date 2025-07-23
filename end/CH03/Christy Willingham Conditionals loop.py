# !/usr/bin/env python3
# example workign with conditionals
# By Christy Willingham
# Write a script that:
#  Asks the user "Is today a good day? (y/n)"
#   Takes input from the user
#   If the answer is "y", print out "Yes it is"

user_name = input("What is your name? ")
print("Hello " + user_name)


    def send_message():
        """Prints yeah it is ten times."""
        for i in range(10):
            print("yeah it is")

def main():
    user_input = input("Is today a good day? (y/m) ")
    if user_input == "y":
        send_message()