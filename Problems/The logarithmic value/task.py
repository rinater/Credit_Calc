import math
x = int(input())
base = int(input())
if  base == 1 or base <= 0:
    print(round(math.log(x), 2))
else:
    print(round(math.log(x, base), 2))
