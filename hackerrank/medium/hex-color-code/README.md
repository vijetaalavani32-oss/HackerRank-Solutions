# Hex Color Code

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

*CSS* colors are defined using a hexadecimal (*HEX*) notation for the combination of Red, Green, and Blue color values (*RGB*).

_Specifications of HEX Color Code_<br>

■ It must start with a '*#*' symbol.<br>
■ It can have $3$ or $6$ digits.<br>
■ Each digit is in the range of $0$ to $F$. ($1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E$ and $F$).<br>
■ $A-F$ letters can be lower case. ($a, b, c, d, e$ and $f$ are also valid digits).

**Examples**  

    Valid Hex Color Codes
    #FFF 
    #025 
    #F0A1FB 
    
    Invalid Hex Color Codes
    #fffabg
    #abcf
    #12365erff

You are given $N$ lines of *CSS* code. Your task is to print all valid _Hex Color Codes_, in order of their occurrence from top to bottom. 

_CSS Code Pattern_
```CSS
Selector
{
	Property: Value;
}

```




**Input Format**

The first line contains $N$, the number of code lines.<br>
The next $N$ lines contains *CSS* Codes.  

__Constraints__

$0 < N < 50$<br>

**Output Format**

Output the color codes with '*#*' symbols on separate lines.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T09:05:01.172Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())
inside = False

for _ in range(n):
    line = input()

    if '{' in line:
        inside = True
        continue

    if '}' in line:
        inside = False
        continue

    if inside:
        colors = re.findall(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?(?![0-9a-fA-F])', line)
        for color in colors:
            print(color)


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/hex-color-code/problem)