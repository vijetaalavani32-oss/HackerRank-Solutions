# Array Mathematics

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

[__floor__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.floor.html#numpy-floor)  
The tool *floor* returns the floor of the input element-wise.  
The floor of $x$ is the largest integer $i$ where $i \le x$. 

    import numpy

    my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    print numpy.floor(my_array)			#[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

[__ceil__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ceil.html#numpy-ceil)  
The tool *ceil* returns the ceiling of the input element-wise.  
The ceiling of $x$ is the smallest integer $i$ where $i \ge x$. 

    import numpy

    my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    print numpy.ceil(my_array)			#[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

[__rint__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.rint.html)  
The *rint* tool rounds to the nearest integer of input element-wise.

    import numpy

    my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    print numpy.rint(my_array)			#[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
    
--- 
__Task__  
You are given a 1-D array, $A$. Your task is to print the $floor$, $ceil$ and $rint$ of all the elements of $A$. 

__Note__  
In order to get the correct output format, add the line $\text{numpy.set_printoptions(legacy='1.13')}$ below the numpy import.  

**Input Format**

A single line of input containing the space separated elements of array $A$. 

**Constraints**

 

**Output Format**

On the first line, print the $floor$ of A.  
On the second line, print the $ceil$ of A.  
On the third line, print the $rint$ of A.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T17:39:44.877Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for i in range(N):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(np.floor_divide(A, B))
print(np.mod(A, B))
print(np.power(A, B))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem)