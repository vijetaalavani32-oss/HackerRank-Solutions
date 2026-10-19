# Any or All

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string $S$.   
$S$ contains alphanumeric characters only.  
![](http://i.imgur.com/u7WkSk7.gif)
Your task is to sort the string $S$ in the following manner:

- All sorted *lowercase letters* are ahead of *uppercase letters*. 
- All sorted *uppercase letters* are ahead of digits.
- All sorted *odd digits* are ahead of sorted *even digits*.



**Input Format**

A single line of input contains the string $S$.



**Constraints**

+ $0 < len(S) < 1000$

**Output Format**

Output the sorted string $S$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T08:18:44.560Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
numbers = input().split()
print(all(int(x) > 0 for x in numbers) and any(x == x[::-1] for x in numbers))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/ginorts/problem)