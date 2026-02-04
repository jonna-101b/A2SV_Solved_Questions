import math
import os
import random
import re
import sys

def checkWeirdness(num):
    if num % 2 != 0:
        print("Weird")
    elif 6 <= num <= 20:
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    checkWeirdness(n)
    
