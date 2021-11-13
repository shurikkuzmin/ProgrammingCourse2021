#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:09:33 2021

@author: shurik
"""
import sys
import numpy

shift = int(input("Please enter the shift for Ceasar cipher: "))

numbers=[0,234,2343,324,3264233426,23462634]
string_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letters = []
for i in range(0, 26):
    letters.append(string_letters[i])

letters = numpy.array(letters)

transformed_letters = numpy.roll(letters, shift)
print(transformed_letters)
#transformed_letters = 26*['A']

#for i in range(shift,26):
#    transformed_letters[i] = letters[i-shift]

#for i in range(0, shift):
#    transformed_letters[i] = letters[26 - shift + i]