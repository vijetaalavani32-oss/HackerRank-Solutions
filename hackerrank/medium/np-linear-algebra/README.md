# Linear Algebra

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The *NumPy* module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module *linalg*.  

[__linalg.det__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html)

The *linalg.det* tool computes the determinant of an array.  

	print numpy.linalg.det([[1 , 2], [2, 1]])		#Output : -3.0

---
[__linalg.eig__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html)

The *linalg.eig* computes the eigenvalues and right eigenvectors of a square array.    

    vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
    print vals										#Output : [ 3. -1.]
    print vecs										#Output : [[ 0.70710678 -0.70710678]
													#		   [ 0.70710678  0.70710678]]
                                                    
---
[__linalg.inv__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html)  

The *linalg.inv* tool computes the (multiplicative) inverse of a matrix.

	print numpy.linalg.inv([[1 , 2], [2, 1]])		#Output : [[-0.33333333  0.66666667]
													#		   [ 0.66666667 -0.33333333]]
                                                    
Other routines can be found [here](http://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

---
__Task__

You are given a square matrix $A$ with dimensions $N $X$ N$. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

**Input Format**

The first line contains the integer $N$.  
The next $N$ lines contains the $N$ space separated elements of array $A$. 

**Constraints**

 

**Output Format**

Print the determinant of $A$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T17:24:55.489Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
N=int(input())
A=[]
for i in range(N):
    row=list(map(float,input().split()))
    A.append(row)
print(round(np.linalg.det(A),2))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/np-linear-algebra/problem)