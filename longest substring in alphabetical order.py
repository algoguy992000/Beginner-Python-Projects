# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s = 'azcbobobegghakl'


maxSub, currentSub, previousChar = '', '', ''
for char in s:
    if char >= previousChar:
        currentSub = currentSub + char
        if len(currentSub) > len(maxSub):
            maxSub = currentSub
    else: currentSub = char
    previousChar = char
print (maxSub)
