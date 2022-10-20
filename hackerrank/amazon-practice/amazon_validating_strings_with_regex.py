#!/bin/python3

from os import environ
from re import compile
from re import match


#
# Write the regular expression in the blank space below
#

#Cases:
#Single chacter from a-b
#a *some characters in between* a
#b * some characters in between* b
#Following syntax from:
#insert website here
#I was able to solve ethis problem following the syntax.


regularExpression = '^[a-b]$|^a.a$|^b.b$'
pattern = compile(regularExpression)

query = int(input())
result = ['False'] * query

for i in range(query):
    someString = input()
    
    if pattern.match(someString):
        result[i] = 'True'

with open(environ['OUTPUT_PATH'], 'w') as fileOut:
    fileOut.write('\n'.join(result))