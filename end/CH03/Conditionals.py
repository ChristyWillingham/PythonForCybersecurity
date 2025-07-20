# !/usr/bin/env python3
# example workign with conditionals
# By Christy Willingham
# Write a script that:
#  Asks the user "Is today a good day? (y/n)"
#   Takes input from the user
#   If the answer is "y", print out "Yes it is"

user_name = input("What is your name? ")
print("Hello " + user_name)

# define the question
today_is_a_good_day = input("Is today a good day? (y/n) ")

if (today_is_a_good_day == "Y"):
    print("Yes it is")

