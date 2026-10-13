# Array Mathematics

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the *NumPy* module. 

    import numpy

    a = numpy.array([1,2,3,4], float)
    b = numpy.array([5,6,7,8], float)

    print a + b                     #[  6.   8.  10.  12.]
    print numpy.add(a, b)           #[  6.   8.  10.  12.]

    print a - b                     #[-4. -4. -4. -4.]
    print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

    print a * b                     #[  5.  12.  21.  32.]
    print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

    print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
    print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

    print a % b                     #[ 1.  2.  3.  4.]
    print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

    print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
    print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
    
---
__Task__  

You are given two integer arrays, $A$ and $B$ of dimensions $N $X$ M$.  
Your task is to perform the following operations:

 1. Add ($A$ + $B$)   
 2. Subtract ($A$ - $B$)  
 3. Multiply ($A$ * $B$)   
 4. Integer Division ($A$ / $B$)  
 5. Mod ($A$ % $B$)  
 6. Power ($A$ ** $B$)
 
__Note__  
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.  

**Input Format**

The first line contains two space separated integers, $N$ and $M$.   
The next $N$ lines contains $M$ space separated integers of array $A$.  
The following $N$ lines contains $M$ space separated integers of array $B$.  

**Constraints**

 

**Output Format**

Print the result of each operation in the given order under **Task**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T17:39:09.725Z  

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

[View on HackerRank](https://www.hackerrank.com/challenges/np-array-mathematics/problem)