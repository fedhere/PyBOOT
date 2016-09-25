###Federica Bianco CUSP NYU 2016
###writtenforPython BootcampSeptember 24 2016
###EXERCISE:
##write a script that prints to standard output "Hallo <Name>" if before 5PM
##prints to standard output "GoodNight <Name>" if before 5PM
##where <Name> is the user name input intline

from __future__ import print_function
import datetime
__author__='__fbb__'

def printContent(timeNow, name = "You"):
    """Creates string to be printed
    Arguments:
    current time as a datetime object
    """

    today5PM = datetime.datetime.now().replace(hour=17, minute=0, second=0, microsecond=0)
    if timeNow < today5PM:
        return "Hello " + name
       
    return "GoodNight " + name

if __name__ == '__main__':
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

