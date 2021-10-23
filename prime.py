#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:46:35 2021

@author: shurik
"""
import sys

number = int(input("Please enter your number? "))

if number < 0:
    print("Please enter the positive number!")
    sys.exit(0)

is_prime_number = True
for i in range(2,number):
    if number % i == 0:
        is_prime_number = False
        print("Number is not a prime number as there is a divider",i)
        break
if is_prime_number == True:
    print("The number is a prime number")
