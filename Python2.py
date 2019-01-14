# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 20:10:02 2018

@author: psarka
"""
# =================================================================================================================
#  1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list.
# =================================================================================================================

entry = input("Input numbers separated by comma: ")
listnum=entry.split(",")
print("List Generated: ",end=" ") 
print(listnum)

# =============================================================================
#  2. Create the below pattern using nested for loop in Python.
# =============================================================================
#
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *


for i in range(5):
    for j in range(1,i+1,1):
            print('*',end='')
    print()
for i in range(5):
    for j in range(5,i,-1):
        print('*',end='')
    print()
    

# =========================================================================================
#  3. Write a Python program to reverse a word after accepting the input from the user.
# =========================================================================================

word = input("Input a word: ")

for i in range(len(word)-1, -1, -1):
  print(word[i], end="")
print("\n")

# =====================================================================================================
#  4.Write a Python Program to print the given string in the format specified in the sample
#   output.
#   WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN,
#   SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens
# =====================================================================================================


print("WE, THE PEOPLE OF INDIA," + "\n\t" + "having solemnly  resolved to constitute India into a SOVEREIGN," +
      "!" + "\n\t\t" + "SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC" + "\n\t\t" + " " 
      + "and to secure to all its citizens")
