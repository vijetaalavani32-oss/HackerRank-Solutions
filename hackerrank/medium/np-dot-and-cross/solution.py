# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
n=int(input())
A=[]
B=[]
for i in range(n):
    row=list(map(int,input().split()))
    A.append(row)
for i in range(n):
    row =list(map(int,input().split()))
    B.append(row)
A=np.array(A)
B=np.array(B)
result=np.dot(A,B)
print(result)
