# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
shape=tuple(map(int,input().split()))

print(np.zeros(shape,dtype=int))
print(np.ones(shape,dtype=int))
