#!/usr/bin/env python
import itertools
# L1=['apple', 'banana', 'pear']
# L2=['car', 'truck']
# L3=['zambia', 'malawi', 'kenya']
# print [[a,b,c] for a in L1 for b in L2 for c in L3]

def user_input(value):
    if isinstance(value, tuple):
        return list(value)
    else:
        user_list = value.split(',')
        numbers = [(x.strip()) for x in user_list]
        return numbers

while True:
    mylist = []
    try:
        i=0
        while True:
            value = raw_input("Please enter no of elements values separated by commas in the list" + str(i+1) + " : ")
            Matrix=user_input(value)
            mylist.append(Matrix)
            val = raw_input("Do you want to create another list (Y/N): ")
            if val != "y" and val != "Y":
                break
            i+=1
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."

    print [[a,b,c] for a in mylist[0] for b in mylist[1] for c in mylist[2]]

    val = raw_input("Do you want to continue (Y/N): ")
    if val != "y" and val != "Y":
        break


