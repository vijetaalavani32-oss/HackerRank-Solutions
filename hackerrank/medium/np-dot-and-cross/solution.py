# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n, m = map(int, input().split())

my_array = []

for i in range(n):
    row = list(map(int, input().split()))
    my_array.append(row)

my_array = np.array(my_array)

print(np.mean(my_array, axis=1))
print(np.var(my_array, axis=0))
print(round(np.std(my_array), 11))
