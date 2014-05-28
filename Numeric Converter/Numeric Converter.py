#!/usr/bin/env python
import num2word

while True:
    try:
       print('Number in words: %s'%(num2word.to_card(int(raw_input("Please enter a number: ")))))
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."

    val = raw_input("Do you want to continue (Y/N): ")
    if val != "y" and val != "Y":
        break