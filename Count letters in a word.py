# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 01:14:11 2016

@author: Home
"""

iteration = 0
count = 0

g = input("Enter a word ")
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in g: 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 