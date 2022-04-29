'''
Federica Bianco CUSP NYU 2016
written for CUSP Python Bootcamp September 24 2016, revised for bootcamp 09/30/2017
EXERCISE:
write a script that prints to standard output "Good Morning <Name>" if before 1PM
prints to standard output "Good Afternoon <Name>" if after 1PM
where <Name> is the user name input intline
'''

from __future__ import print_function
import datetime
import sys
__author__='__fbb__'

def printContent(timeNow, name = "You"):
    """Creates string to be printed
    Arguments:
    current time as a datetime object
    """

    today1PM = datetime.datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)
    if timeNow < today1PM:
        return "Good Morning " + name
       
    return "Good Afternoon " + name

if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1] == 'help') or len(sys.argv) == 1:
        print ('''
    write a script that prints to standard output "Good Morning <Name>" if before 1PM
    prints to standard output "Good Afternoon <Name>" if after 1PM
    where <Name> is the user name input intline
    
    if you can: make sure it works with both python 2 and 3
    hints: 
    - you can use raw_input/input to accept arguments upon request.
    - you can use the datetime package to check the time of the day
    - you can use try/except if you come across functions that work differently in python2 vs python3
    
    ''')
        exit()
    try:
        #this would workin Python2
        yourName = raw_input("What's your name?")
    except NameError:
        #this would workin Python3
        yourName = input("What's your name?")
    if yourName == '':        
        print(printContent(datetime.datetime.now()))
    else:
        print(printContent(datetime.datetime.now(), yourName))

