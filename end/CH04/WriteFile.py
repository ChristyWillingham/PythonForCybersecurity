#!/usr/bin/env python3
# Sample script that writes to a file
# By Christy Willingham

# open file for writing - 'f' is commonly used to reference a file
f = open("hackme.txt", "w")

# write content and save it to the file
first_name = input("What is your first name?")
favorite_color = input("What is your favorite color?")
pets_name = input("What was your first pet's name?")
mothers_manden = input("What is your mother's maiden name?")
elementary_school = input("What elementary school did you attend?")
f.write("I see your first name is: " + first_name + "\n" )
f.write("I see your favorite color is: " + favorite_color + "\n" )
f.write("I see your first pet's name is: " + pets_name + "\n" )
f.write("I see your mother's maiden name is: " + mothers_manden + "\n" )
f.write("I see the elementary school you attended was: " + elementary_school + "\n") 
# close the file
f.close()

print ("Here is someone to hack - information")
print (first_name)
print (favorite_color)
print (pets_name)
print (mothers_manden)
print (elementary_school)
