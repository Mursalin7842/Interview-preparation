#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
is_wierd = n % 2
if n >= 1 and n <= 100:
    if is_wierd:
        print("Weird")
    elif is_wierd == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif is_wierd == 0 and 6 <= n <= 20:
        print("Weird")
    elif is_wierd == 0 and 20 < n:
        print("Not Weird")
