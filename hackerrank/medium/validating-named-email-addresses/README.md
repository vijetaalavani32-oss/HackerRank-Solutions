# Validating and Parsing Email Addresses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A valid email address meets the following criteria:  

- It's composed of a *username*, *domain* name, and *extension* assembled in this format: `username@domain.extension ` 
- The *username* starts with an *English alphabetical character*, and any subsequent characters consist of one or more of the following: [alphanumeric characters](https://en.wikipedia.org/wiki/Alphanumeric), `-`,`.`, and `_`.  
- The *domain* and *extension* contain only [English alphabetical characters](https://en.wikipedia.org/wiki/English_alphabet).  
- The *extension* is $1$, $2$, or $3$ characters in length.

Given $n$ pairs of names and email addresses as input, print each name and email address pair having a *valid* email address on a new line.

**Hint:** Try using [Email.utils()](https://docs.python.org/2/library/email.util.html#module-email.utils) to complete this challenge. For example, this code: 

```python
import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
```
produces this output:

    ('DOSHI', 'DOSHI@hackerrank.com')
    DOSHI <DOSHI@hackerrank.com>

**Input Format**

The first line contains a single integer, $n$, denoting the number of email address.  	
Each line $i$ of the $n$ subsequent lines contains a *name* and an *email address* as two space-separated values following this format:

	name <user@email.com>


**Constraints**

- $ 0 \lt n \lt 100$  

**Output Format**

Print the space-separated name and email address pairs containing *valid* email addresses only. Each pair must be printed on a new line in the following format:

	name <user@email.com>

You must print each valid email address in the same order as it was received as input.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T09:02:43.268Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import email.utils

n = int(input())
for _ in range(n):
    name, addr = input().split()
    email_addr = email.utils.parseaddr(addr)[1]
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}", email_addr):
        print(email.utils.formataddr((name, email_addr)))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/validating-named-email-addresses/problem)