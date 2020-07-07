#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the hourglassSum function below.
def hourglassSum(arr):
    s=0
    l=[]                                        #initializing a list 
    for i in range(0,4):                        #running the loop for 4 times
        for j in range(0,4):                    #same loop running for 4 times
            s=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]   #getting the required sum by adding all the required positions
            l.append(s)                         #entering the sum for one part it into the list
            s=0                                 #making s zero
    return(max(l))                              #at last returning the maximum for the list
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
