# Input()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The `eval()` expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.  

For example:  

```python
>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
```
    
Here, `eval()` can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings.  

For example:

```python
>>> type(eval("len"))
<type 'builtin_function_or_method'>
```

Without eval()

```python
>>> type("len")
<type 'str'>
```
    
**Task**  
You are given an expression in a line. Read that line as a string variable, such as *var*, and print the result using *eval(var)*.  

**NOTE**: Python2 users, please import `from __future__ import print_function`.  

**Constraint**  
Input string is less than 100 characters.  

**Sample Input**  

	print(2 + 3)

**Sample Output**  

	5
    
    
<!-- In Python2, input() function works equivalent to eval(raw_input()) do give it a try.  -->


**Input Format**

 

**Constraints**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T05:30:32.074Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOU

x, y = map(int, input().split())
polynomial = input()

print(eval(polynomial) == y)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-eval/problem)