#!/usr/bin/env python

def numcount(value):
    number = ','.join(str(i) for i in xrange(1,value) if not str(i).__contains__("7") in (1,7))
    counts = 0
    if(number != ""):
        counts = len(number.split(','))
    print('Number: %s'%(number))
    print('Number Counts: %d'%(counts))

while True:
    try:
        numcount(int(raw_input("Please enter a number: ")))
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."

    val = raw_input("Do you want to continue (Y/N): ")
    if val != "y" and val != "Y":
        break