# This program will generate a random password which will be hard to be brute-forced
# Credit to: HACKERXGUY

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_chars = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

combination = lower_case + upper_case + numbers + special_chars

while True:
    try:
        length_for_pwd = int(input("Please input the desired length of password (8-16): "))
        pwd = "".join(random.sample(combination, length_for_pwd))
        print("Success!")
        print("Generated password:", pwd)
    except ValueError:
        print("You have entered an invalid value. Please try again.")
        continue
    else:
        break
