#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    res=s[0].upper()
    for i in range(len(s)-1):
        a = s[i+1]
        if s[i] == ' ':
            res += a.upper()
        else:
            res += a
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# input:
# chris alan
# 1 w 2 r 3g

# output:
# Chris Alan
# 1 W 2 R 3g
