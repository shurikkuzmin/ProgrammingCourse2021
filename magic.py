#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 09:50:43 2021

@author: shurik
"""
import sys

# Find all magic numbers less or equal 1000
for number in range(2,1001):
    sum_dividers = 0    
    for i in range(1, number):
        if number % i == 0:
            sum_dividers = sum_dividers + i
    
    if sum_dividers == number:
        print("Number ", number, "is the magic number!")
