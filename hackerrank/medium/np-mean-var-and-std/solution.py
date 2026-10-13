# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n, m = map(int, input().split())

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

arr = np.array(arr)

minimums = np.min(arr, axis=1)
answer = np.max(minimums)

print(answer)
