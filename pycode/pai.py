import sys
import math
from decimal import *

getcontext().prec = 20000
'def bbp(n):'
pai = Decimal(0)
k = 0
while k < 20000:
    pai += (Decimal(1) / (16 ** k)) * ((Decimal(4) / (8 * k + 1)) - (Decimal(2) / (8 * k + 4)) - (Decimal(1) / (8 * k + 5)) - (
                     Decimal(1) / (8 * k + 6)))
    k += 1
L = str(pai)
for i in range(10):
    print(L.count(str(i)),i)
print(L)



'''def main(argv):
    if len(argv) != 2:
        sys.exit('Usage: BaileyBorweinPlouffe.py <prec> <n>')
getcontext().prec = (int(sys.argv[1]))
my_pi = bbp(int(sys.argv[2]))
accuracy = 100 * (Decimal(math.pi) - my_pi) / my_pi
print("Pi is approximately " + str(my_pi))
print("Accuracy with math.pi: " + str(accuracy))
if __name__ == "__main__":
    main(sys.argv[1:])'''