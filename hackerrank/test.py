
#!/bin/python3
from operator import itemgetter
import math
import os
import random
import re
import sys



#
# Complete the 'groupSort' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def groupSort(arr):
    #Note: Ideally we can separate each part into functions so that we can take advantage
    #of modularity and code reusability. Comments will be limited as this is a timed session.
    
    #Initial variables
    n = len(arr)
    two_d_arr = [[0 for x in range(3)] for y in range(n)] #Create a 2 d array that is space efficient
    
    #For every value in the arr go through and count the freq
    #We will arrange the analysis as distinct value:[distinct value][frequency]
    for value in arr:
        two_d_arr[value][1] += 1
        two_d_arr[value][0] = value
        
    #Assuming we have a 2D array that contains the distinct value with it's frequency
    #We want to sort the array in descending order.
    sorted_results = sorted(two_d_arr, key=itemgetter(1), reverse=True)
        
    #Assuming we have a sorted 2D array that was sorted by the second column:
    #Let's get rid of the extra rows that have 0. We will first count so that
    #we don't waste time copying the array multiple times. Ex. using append()
    count = 0
    for row in sorted_results:
        if row[0] != 0:
            count += 1
    
    
    final_results = [[0 for x in range(2)] for y in range(count)]
    index = 0
    while index < count:
        final_results[index] = sorted_results[index]
        index += 1
        
    print("test")
    
        
    return final_results
        
    

groupSort(arr=[7,12,3])