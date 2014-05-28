#!/usr/bin/env python

import string

def rot13(value):
    rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return string.translate(value, rot13)
            
while True:     
    values=raw_input("Enter your values :").split(' ')
    rot13value = []    
    for index,value in enumerate(values):
        if ((index+1)%2)==1:
            value=value[::-1]
        rot13value.append(rot13(value))
    print('rot13 version values: %s'%(" ".join(rot13value)))
    val = raw_input("Do you want to continue (Y/N): ")
    if val != "y" and val != "Y":
        break
