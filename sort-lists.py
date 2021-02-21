# -*- coding: utf-8 -*-
"""
Takes a list of integers, for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and prints out a list with all the integers of the list
that are less than a number given by the user
and another list with the remaining integers.

If an incorrect number is given,
user has a second chance to enter the number.

@author: Barbora Doslikova
"""
  
sample = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def listSorter(sampleList, compareInt):
        correctOutput = []
        incorrectOutput = []
        
        for i in sampleList:
            if i < compareInt:
                correctOutput.append(i)
            else:
                incorrectOutput.append(i)   
        print(correctOutput, incorrectOutput)

try:
    comparator = int(input("Give a whole number: "))
except ValueError:
    comparator = int(input("Give a *whole number*: "))

listSorter(sample, comparator)

