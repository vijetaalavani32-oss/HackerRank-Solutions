# Map and Lambda Function

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer $N$ followed by $N$ email addresses. Your task is to print a list containing only *valid* email addresses in lexicographical order.<br><br>

Valid email addresses must follow these rules:

- It must have the *username@websitename.extension* format type.
- The username can only contain letters, digits, dashes and underscores $[a-z], [A-Z], [0-9], [\_-]$. 
- The website name can only have letters and digits $[a-z], [A-Z], [0-9]$. 
- The extension can only contain letters $[a-z], [A-Z]$.   
- The maximum length of the extension is $3$.
<br><br>

**Concept**

A *filter* takes a function returning *True* or *False* and applies it to a sequence, returning a list of only those members of the sequence where the function returned *True*. A *Lambda* function can be used with filters.
<br><br>
Let's say you have to make a list of the squares of integers from $0$ to $9$ (both included).<br>

    >> l = list(range(10))
	>> l = list(map(lambda x:x*x, l))

Now, you only require those elements that are greater than $10$ but less than $80$.<br>

	>> l = list(filter(lambda x: x > 10 and x < 80, l))

Easy, isn't it?

**Example**   

Complete the function *fun* in the editor below.   

*fun* has the following paramters:   

- *string s:* the string to test   

**Returns**   

- *boolean:* whether the string is a valid email or not   

**Input Format**

The first line of input is the integer $N$, the number of email addresses. <br>
$N$ lines follow, each containing a string.



**Constraints**

Each line is a non-empty string.

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T12:42:54.003Z  

```py
cube = lambda x:x**3# complete the lambda function 

def fibonacci(n):
    result = []
    a, b = 0, 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


    # return a list of fibonacci numbers


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem)