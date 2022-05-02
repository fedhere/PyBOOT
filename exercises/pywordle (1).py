# -*- coding: utf-8 -*-
"""pywordle.py


python version of the Wordle game

simple string manipulation exercise

Written by FBB April 2022 for PyBOOT
"""
import wordle
word = wordle.word

def comparestrings(guess, word=word):
  result = ['_', '_', '_', '_', '_']
  if not len(guess) == len(word):
    print("word must be 5 characters")
    return
  for i in range(len(word)):
    if guess[i] == word[i]:
      result[i] = guess[i]
    elif guess[i] in word:
      result[i] = '*'
  #print(list(word))
  
  if not '_' in result and not '*' in result:
    print ("GENIUS!! you did it!!")
  else :
    print(list(guess))
    print(result)
    print ("try again...")

