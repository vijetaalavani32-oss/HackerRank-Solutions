# Validating UID

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

*ABCXYZ* company has up to $100$ employees.  
The company decides to create a unique identification number (UID) for each of its employees.  
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:  

- It must contain at least $2$ uppercase English alphabet characters.   
- It must contain at least $3$ digits ($0$ - $9$).  
- It should only contain alphanumeric characters ($a$ - $z$, $A$ - $Z$ & $0$ - $9$).  
- No character should repeat.  
- There must be exactly $10$ characters in a valid UID.

**Input Format**

The first line contains an integer $T$, the number of test cases.  
The next $T$ lines contains an employee's UID.

**Output Format**

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T09:08:49.958Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

for _ in range(n):
    uid = input()

    if (len(uid) == 10
        and len(set(uid)) == 10
        and len(re.findall(r'[A-Z]', uid)) >= 2
        and len(re.findall(r'[0-9]', uid)) >= 3
        and uid.isalnum()):
        print("Valid")
    else:
        print("Invalid")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/validating-uid/problem)