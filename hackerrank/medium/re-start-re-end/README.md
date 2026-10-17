# Re.findall() & Re.finditer()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

###<sub>[start() & end()](https://docs.python.org/2/library/re.html#re.MatchObject.start)</sub>

These expressions return the indices of the *start* and *end* of the substring matched by the group.

<sub>__Code__</sub>  

    >>> import re
    >>> m = re.search(r'\d+','1234')
    >>> m.end()
    4
    >>> m.start()
    0
    
---
__Task__  
You are given a string $S$.  
Your task is to find the indices of the *start* and *end* of string $k$ in $S$.

**Input Format**

The first line contains the string $S$.  
The second line contains the string $k$.

__Constraints__  

$ 0 < len(S) < 100$  
$ 0 < len(k) < len(S)$

**Output Format**

Print the tuple in this format: (_start_ __index_, _end_ __index_).   
If no match is found, print `(-1, -1)`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T12:50:28.950Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
s = input()

matches = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])[aeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])', s, re.IGNORECASE)

if matches:
    print(*matches, sep='\n')
else:
    print(-1)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/re-start-re-end/problem)