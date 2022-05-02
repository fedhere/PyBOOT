# -*- coding: utf-8 -*-
"""pywordle.py


python version of the Wordle game

simple string manipulation exercise

Written by FBB April 2022 for PyBOOT
"""


def comparestrings(guess, word=None):
  """ compares a given 5-character string with a chosen target letter by letter
  
  Input:
    guess: 5-character string - the users guess
    word (optional): 5-character string - the target - if a string is not passed the code looks for a "wordle.py" module with the definition of word
    
  Output:
    returns a string with each correct character in the right place visible, each correct chaeracter in the wrong place marked by a "*"
  """
  result = ['_', '_', '_', '_', '_']
  
  # get the target word
  if word is None:
    import wordle
    word = wordle.word
    
  #set both guess and target to upper case
  word = word.upper()
  guess = guess.upper()

  #check word length first
  if not len(guess) == len(word):
    print("word must be 5 characters")
    return
  for i in range(len(word)):
    if guess[i] == word[i]:
      result[i] = guess[i]
    elif guess[i] in word:
      result[i] = '*'

  #check and validate each letter
  if not '_' in result and not '*' in result:
    print ("GENIUS!! you did it!!")
  else :
    print(list(guess))
    print(result)
    print ("try again...")

