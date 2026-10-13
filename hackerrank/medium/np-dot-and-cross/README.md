# Dot and Cross

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

[__dot__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html)

The *dot* tool returns the dot product of two arrays.

    import numpy

    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])

    print numpy.dot(A, B)		#Output : 11
    
[__cross__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.cross.html)

The *cross* tool returns the cross product of two arrays.

	import numpy

    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])

    print numpy.cross(A, B)		#Output : -2
    
---
__Task__

You are given two arrays $A$ and $B$. Both have dimensions of $N $X$ N$.  
Your task is to compute their [matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication#Matrix_product_.28two_matrices.29).

**Input Format**

The first line contains the integer $N$.  
The next $N$ lines contains $N$ space separated integers of array $A$.  
The following $N$ lines contains $N$ space separated integers of array $B$.

**Output Format**

Print the matrix multiplication of $A$ and $B$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T15:23:24.279Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n = int(input())

A = []
B = []

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

print(np.dot(A, B))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/np-dot-and-cross/problem)