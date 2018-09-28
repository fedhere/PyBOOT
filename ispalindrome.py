## FBB written for python bootcamp CUSP 2016-2017
## function that checks if a string is a palindrom
def lookForPal(string):
    '''Verifies if a string is a palindrom
    Argument:
        a string
    '''
    # I use the method .lower to de-capitalise characters in the input string
    # that way I can just compare if the string and its reverse are the same
    # if I didnt do that Hannah would not look like a palindrom
    if string.lower() == string.lower()[::-1]: 
         # I need to make sure I print the unique half of the word 
         # whether it has even or odd number of characters
        if len(string) % 2 :
            halfpal = string[:int(len(string) / 2 + 1)]
        else: 
            halfpal = string[:int(len(string) / 2)] 
        
        halfpal = string[:int((float(len(string)) / 2.0) + 0.5)]
        print ("Yes its a palindrome", halfpal)
        return (1)
    print ("this is not a palindrome")
    return (-1)