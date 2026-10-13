# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
N=int(input())
A=[]
for i in range(N):
    row=list(map(float,input().split()))
    A.append(row)
print(round(np.linalg.det(A),2))
