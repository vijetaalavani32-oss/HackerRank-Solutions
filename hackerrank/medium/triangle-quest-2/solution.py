# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)

print(np.transpose(arr))
print(arr.flatten())
