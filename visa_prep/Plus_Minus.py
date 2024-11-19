#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zeros = 0
    pos = 0
    neg = 0
    n = len(arr)
    for i in range(n):
        if(arr[i]==0):
            zeros = zeros + 1
        elif(arr[i]>0):
            pos = pos+1
        else:
            neg = neg+1
    print("{:.6f}".format(pos/n))
    print("{:.6f}".format(neg/n))
    print("{:.6f}".format(zeros/n))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
