#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:09:33 2021

@author: shurik
"""
import sys
import numpy

string_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = []
for i in range(0, 26):
    letters.append(string_letters[i])
letters = numpy.array(letters)

shift = int(input("Please enter the shift for Ceasar cipher: "))
transformed_letters = numpy.roll(letters, shift)

def cryptoLine(line):
    transformed_line = ""
    for letter in line:
        my_letter = letter
        if letter.islower():
            my_letter = letter.capitalize()
        my_index = -1
        for index in range(26):
            if my_letter == letters[index]:
                my_index = index
                break
            
        if my_index != -1:
            if letter.islower():
                transformed_line = transformed_line + transformed_letters[my_index].lower() 
            else:
                transformed_line = transformed_line + transformed_letters[my_index]
        else:
            transformed_line = transformed_line + letter
    return transformed_line

f = open("dracula2.txt")
f2 = open("dracula_decoded.txt","w")

for line in f.readlines():
    f2.write(cryptoLine(line))
f.close()
f2.close()
    
