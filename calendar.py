#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:14:06 2021

@author: shurik
"""
import sys

day = int(input("What is your day of birth? "))
month = input("What is your month of birth? ")

if day < 1 or day > 31:
    print("Error: Please enter the day between 0 and 31")
    sys.exit(0)
    
if month.upper() == "JANUARY":
    if day < 21:
        print("Capricorn")
    else:
        print("Aquarius")
elif month.upper() == "FEBRUARY":
    if day < 20:
        print("Aquarius")
    elif day < 29:
        print("Pisces")
    else:
        print("Error: February contains only days from 1 to 28")
        sys.exit(0)
elif month.upper() == "MARCH":
    if day < 21:
        print("Pisces")
    else:
        print("Aries")
elif month.upper() == "APRIL":
    if day < 20:
        print("Aries")
    elif day < 31:
        print("Taurus")
    else:
        print("Error: April contains only days from 1 to 30")
elif month.upper() == "MAY":
    if day < 22:
        print("Taurus")
    else:
        print("Gemini")
elif month.upper() == "JUNE":
    if day < 22:
        print("Gemini")
    elif day < 31:
        print("Cancer")
    else:
        print("Error: June contains only days from 1 to 30")
        sys.exit(0)
elif month.upper() == "JULY":
    if day < 23:
        print("Cancer")
    else:
        print("Leo")
elif month.upper() == "AUGUST":
    if day < 22:
        print("Leo")
    else:
        print("Virgo")
elif month.upper() == "SEPTEMBER":
    if day < 24:
        print("Virgo")
    elif day < 31:
        print("Libra")
    else:
        print("Error: September contains only days from 1 to 30")
        sys.exit(0)
elif month.upper() == "OCTOBER":
    if day < 24:
        print("Libra")
    else:
        print("Scorpio")
elif month.upper() == "NOVEMBER":
    if day < 23:
        print("Scorpio")
    elif day < 31:
        print("Sagittarius")
    else:
        print("Error: November contains only days from 1 to 30")
        sys.exit(0)
elif month.upper() == "DECEMBER":
    if day < 23:
        print("Sagittarius")
    else:
        print("Capricorn")
else:
    print("Error: Please enter the proper name of the month")

