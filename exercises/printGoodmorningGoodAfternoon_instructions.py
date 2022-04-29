'''
Federica Bianco CUSP NYU 2016
written for CUSP Python Bootcamp September 24 2016, 
revised for bootcamp 09/30/2017, 
revised for bootcamp 09/28/2018
EXERCISE: 
write a script that prints to standard output "Good afternoon <Name>" if before 6PM
prints to standard output "Good evening <Name>" if after 6PM
where <Name> is the user name input intline
'''

from __future__ import print_function
import sys
import datetime
__author__='__fbb__'

def printContent(timeNow, name = "You"):
    """Creates string to be printed
    Arguments:
    current time as a datetime object
    """
    greetings = ...
    
    return greetings

if __name__ == '__main__':
    #sys.argv is the container that holds all arguments passed to python
    # it is a list
    if (len(sys.argv) > 1 and sys.argv[1] == 'help') or len(sys.argv) == 1:
        print ('''
    write a script that prints to standard output "Good Afternoon <Name>" if before 6PM
    prints to standard output "Good Evening <Name>" if after 6PM
    where <Name> is the user name input intline
    
    if you can: make sure it works with both python 2 and 3
    hints: 
    - you can use raw_input/input to accept arguments upon request.
    - you can use the datetime package to check the time of the day
    - you can use try/except if you come across functions that work differently in python2 vs python3
    
    ''')
        sys.exit()
    try:
        #this would workin Python2
        yourName = ...
    except NameError:
        #this would workin Python3
        yourName = ...
    print(printContent(...))

