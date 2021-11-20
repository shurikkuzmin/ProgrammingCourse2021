#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:09:33 2021

@author: shurik
"""
import sys
import numpy

shift = int(input("Please enter the shift for Ceasar cipher: "))

text = input("Please enter your text to encode: ")

string_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letters = []
for i in range(0, 26):
    letters.append(string_letters[i])

letters = numpy.array(letters)

transformed_letters = numpy.roll(letters, shift)


transformed_text = ""
for letter in text:
    my_letter = letter
    if letter.islower():
        my_letter = letter.capitalize()
    my_index = -1
    for index in range(26):
        if my_letter == letters[index]:
            my_index = index
            break
        
    if my_index != -1:
        transformed_text = transformed_text + transformed_letters[my_index]
    else:
        transformed_text = transformed_text + letter
print(text)
print(transformed_text)
#transformed_letters = 26*['A']

#for i in range(shift,26):
#    transformed_letters[i] = letters[i-shift]

#for i in range(0, shift):
#    transformed_letters[i] = letters[26 - shift + i]