# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
n = int(input())
d = OrderedDict()
for _ in range(n):
    name, price = input().rsplit(" ", 1)
    d[name] = d.get(name, 0) + int(price)
for name, price in d.items():
    print(name, price)
