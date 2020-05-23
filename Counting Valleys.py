#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):    
    sum=0
    count=0
    for i in s:
        if(i=='U'):
            sum+=1
        else:
            sum-=1
        if(sum==0 and i=='U'):
            count+=1            
    return(count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
