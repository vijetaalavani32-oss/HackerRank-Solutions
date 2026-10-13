# Dot and Cross

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

[__inner__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.inner.html)  

The *inner* tool returns the [inner product](https://en.wikipedia.org/wiki/Inner_product_space) of two arrays.

    import numpy

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.inner(A, B)		#Output : 4
    
[__outer__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.outer.html)    

The *outer* tool returns the [outer product](https://en.wikipedia.org/wiki/Outer_product) of two arrays.

    import numpy

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.outer(A, B)		#Output : [[0 0]
 								#		   [3 4]]
                                
---
__Task__  

You are given two arrays: $A$ and $B$.  
Your task is to compute their *inner* and *outer* product.

**Input Format**

The first line contains the space separated elements of array $A$.  
The second line contains the space separated elements of array $B$.


**Output Format**

First, print the inner product.  
Second, print the outer product.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T15:17:34.113Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/np-inner-and-outer/problem)