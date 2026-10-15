# Concatenate

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

__[zeros](http://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html#numpy-zeros)__

The *zeros* tool returns a new array with a given shape and type filled with $0$'s.

    import numpy

    print numpy.zeros((1,2))                    #Default type is float
    #Output : [[ 0.  0.]] 

    print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
    #Output : [[0 0]]
    
__[ones](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ones.html#numpy-ones)__

The *ones* tool returns a new array with a given shape and type filled with $1$'s.

    import numpy

    print numpy.ones((1,2))                    #Default type is float
    #Output : [[ 1.  1.]] 

    print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
    #Output : [[1 1]]   
    
---
**Task**  

You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools `numpy.zeros` and `numpy.ones`.

**Input Format**

A single line containing the space-separated integers.

**Constraints**

$1 \le \text{each integer} \le 3$

**Output Format**

First, print the array using the `numpy.zeros` tool and then print the array with the `numpy.ones` tool.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T06:10:13.196Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
N, M, P = map(int, input().split())

array_1 = np.array([input().split() for _ in range(N)], int)
array_2 = np.array([input().split() for _ in range(M)], int)

print(np.concatenate((array_1, array_2), axis=0))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/np-zeros-and-ones/problem)