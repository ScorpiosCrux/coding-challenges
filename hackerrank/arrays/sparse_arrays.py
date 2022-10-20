#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#


#Test input is like:
#strings = ["def", "de", "fgh"]
#queries = ["de", "lmn", "fgh"]

#Output would be like:
#results = [1, 0, 1]

def matchingStrings(strings, queries):
    num_of_queries = len(queries)
    results = [0 for x in range(num_of_queries)]
    
    
    for i in range(num_of_queries):
        query = queries[i]
        if query in strings:
            results[i] += strings.count(query)
        
            
    return results
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
