# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 23:27:32 2022

@author: echua
"""

# This function is used to generate random password based on user input

import string
import random

# Character library for password generator
characters = list(string.digits + string.ascii_letters + "!@#$%^&*()")

def generate_password():
    # User to input length of password to be generated
    pass_length = int(input('Please input the length of password: '))
    
    # Shuffle the characters
    random.shuffle(characters)
    
    # Start to generate password
    password = []
    for i in range(pass_length):
        password.append(random.choice(characters))
        
    # Shuffle the generated password
    random.shuffle(password)
    
    # Join and print the password
    password = "".join(password)
    print("The generated password is " + password)

# Run the function
generate_password()