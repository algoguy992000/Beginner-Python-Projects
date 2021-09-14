# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s = "bobhjgkhjhgjbob"
countBob = 0
for i in range(len(s)):
    if s[i:].startswith('bob'):
        countBob += 1
print('Number of times bob occurs is: ' + str(countBob))