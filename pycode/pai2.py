import sys
import math
from decimal import *

def bbp(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1) / (16 ** k)) * (
                    (Decimal(4) / (8 * k + 1)) - (Decimal(2) / (8 * k + 4)) - (Decimal(1) / (8 * k + 5)) - (
                        Decimal(1) / (8 * k + 6)))
        k += 1
    return pi
n = int(input('please input'))
getcontext().prec = n
L = str(bbp(n))
for i in range(10):
    print(L.count(str(i)),i)
print(L)








