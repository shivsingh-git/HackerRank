#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the 'fizzBuzz' function below.
# The function accepts INTEGER n as parameter.
def fizzBuzz(n):
    for x in range(1,n+1):
     if x%15==0:print("FizzBuzz")
     elif x%3==0:print("Fizz")
     elif x%5==0:print("Buzz")
     else:print(x)
if __name__ == '__main__':
