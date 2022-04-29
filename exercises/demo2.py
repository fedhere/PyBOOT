from __future__ import print_function
import datetime
import sys

#if __name__ == '__main__':
print("this is the main")
try:
    myname = raw_input("who are you?")
except NameError:
    myname = input("who are you?")
    
print("ok %s"%myname)
        
        
