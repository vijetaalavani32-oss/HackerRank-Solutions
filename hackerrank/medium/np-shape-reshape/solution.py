# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
arr=list(map(int,input().split()))
arr=np.array(arr)
arr=np.reshape(arr,(3,3))
print(arr)
