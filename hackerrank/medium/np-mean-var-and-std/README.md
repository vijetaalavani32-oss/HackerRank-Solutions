# Min and Max

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

[__mean__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html)   

The *mean* tool computes the arithmetic mean along the specified axis.  

    import numpy

    my_array = numpy.array([ [1, 2], [3, 4] ])

    print numpy.mean(my_array, axis = 0)		#Output : [ 2.  3.]
    print numpy.mean(my_array, axis = 1)		#Output : [ 1.5  3.5]
    print numpy.mean(my_array, axis = None)		#Output : 2.5
    print numpy.mean(my_array)					#Output : 2.5
    
By default, the axis is `None`. Therefore, it computes the mean of the flattened array.

[__var__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html#numpy-var)  

The *var* tool computes the arithmetic variance along the specified axis.  

    import numpy

    my_array = numpy.array([ [1, 2], [3, 4] ])

    print numpy.var(my_array, axis = 0)			#Output : [ 1.  1.]
    print numpy.var(my_array, axis = 1)			#Output : [ 0.25  0.25]
    print numpy.var(my_array, axis = None)		#Output : 1.25
    print numpy.var(my_array)					#Output : 1.25
    
By default, the axis is `None`. Therefore, it computes the variance of the flattened array.

[__std__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html#numpy.std)  

The *std* tool computes the arithmetic standard deviation along the specified axis.  

    import numpy

    my_array = numpy.array([ [1, 2], [3, 4] ])

    print numpy.std(my_array, axis = 0)			#Output : [ 1.  1.]
    print numpy.std(my_array, axis = 1)			#Output : [ 0.5  0.5]
    print numpy.std(my_array, axis = None)		#Output : 1.11803398875
    print numpy.std(my_array)					#Output : 1.11803398875
    
By default, the axis is `None`. Therefore, it computes the standard deviation of the flattened array.

---
__Task__ 

You are given a 2-D array of size $N $X$ M$.   
Your task is to find:

1. The mean along axis $1$
2. The var along axis $0$
3. The std along axis $None$

**Input Format**

The first line contains the space separated values of $N$ and $M$.  
The next $N$ lines contains $M$ space separated integers.

**Constraints**

 

**Output Format**

First, print the *mean*.  
Second, print the *var*.  
Third, print the *std*.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T14:58:22.617Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/np-mean-var-and-std/problem)