from __future__ import print_function
import datetime
__author__='__fbb__'

def printContent(timeNow):
    """Creates string to be printed
    Arguments:
    current time as a datetime object
    """

    today5PM = datetime.datetime.now().replace(hour=17, minute=0, second=0, microsecond=0)
    if timeNow < today5PM:
        return "Hello World"
       
    return "GoodNight World"

if __name__ == '__main__':
    print(printContent(datetime.datetime.now()))

