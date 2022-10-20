#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

arr =   [[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]


def hourglassSum(arr):
    
    """ #each hour glass has 7 elements lowest value is -9, thus 7 * -9 is the min starting value
    maxValue = 7 * -9
    
    #Since there are not that many possibilities, brute forcing is allowed
    for i in range(6):
        for j in range(6):
            
            #add the top
            top = arr[i][j] + arr[i][j+1] +  """


    # want to find the maximum hourglass sum
    # minimum hourglass sum = -9 * 7 = -63
    maxSum = -63
    
    for i in range(4):
        for j in range(4):
        
            # sum of top 3 elements
            top = sum(arr[i][j:j+3])
            
            # sum of the mid element
            mid = arr[i+1][j+1]
            
            # sum of bottom 3 elements
            bottom = sum(arr[i+2][j:j+3])
            
            hourglass = top + mid + bottom
            
            if hourglass > maxSum:
                maxSum = hourglass
                
    return maxSum
            


hourglassSum(arr)


array_test = [1,2,3,4,5]
test = array_test[0:3]

print ("Done")