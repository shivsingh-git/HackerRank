import math
import os
import random
import re
import sys
def solve(s):                         #definig a function
  for x in s[:].split():              #checking in the string after splitting it just after the spaces
     s = s.replace(x, x.capitalize()) #if the split is found then replacing that x with a capitalize x
  print(s)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = raw_input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
