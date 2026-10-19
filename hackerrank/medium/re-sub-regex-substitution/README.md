# Regex Substitution

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The *re.sub()* tool (_sub_ stands for _substitution_) evaluates a pattern and, for each valid match, it calls a *method* (or *lambda*).  
The *method* is called for all matches and can be used to modify strings in different ways.  
The *re.sub()* method returns the modified string as an output.
 
Learn more about [$re.sub()$](https://docs.python.org/2/library/re.html#re.sub).

__Transformation of Strings__  

 __<sub>Code</sub>__  

 	import re
    
 	#Squaring numbers
    def square(match):
    	number = int(match.group(0))
 		return str(number**2)
 	
    print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
    
        
 __<sub>Output</sub>__  

    1 4 9 16 25 36 49 64 81

<br>
__Replacements in Strings__

  __<sub>Code</sub>__  

	import re

    html = """
    <head>
    <title>HTML</title>
    </head>
    <object type="application/x-flash" 
      data="your-file.swf" 
      width="0" height="0">
      <!-- <param name="movie"  value="your-file.swf" /> -->
      <param name="quality" value="high"/>
    </object>
    """

    print re.sub("(<!--.*?-->)", "", html) #remove comment
    
    
 __<sub>Output</sub>__
    
    <head>
    <title>HTML</title>
    </head>
    <object type="application/x-flash" 
      data="your-file.swf" 
      width="0" height="0">

      <param name="quality" value="high"/>
    </object>

---
__Task__

You are given a text of $N$ lines. The text contains `&&` and `||` symbols.  
Your task is to modify those symbols to the following:  

	&& → and
    || → or


Both `&&` and `||` should have a _space_ " " on both sides. 

**Input Format**

 The first line contains the integer, $N$.  
 The next $N$ lines each contain a line of the text.
 
 __Constraints__
 
 $0 < N < 100$  
 
 Neither `&&` nor `||` occur in the *start* or *end* of each line. 

**Output Format**

 Output the modified text.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T13:53:28.327Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

for _ in range(n):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem)