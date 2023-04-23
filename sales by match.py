import math
import os
import random
import re
import sys

# n= 7
# ar=[1,2,1,2,1,3,2]

def sockMerchant(n, ar):
    count =[]
    for sock in set(ar):
        count.append(ar.count(sock))
    return sum ([i//2 for i in count])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
