# Validating Roman Numerals

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print *True*. Otherwise, print *False*. Try to create a regular expression for a valid Roman numeral.

**Input Format**

A single line of input containing a string of Roman characters.

**Output Format**

Output a single line containing *True* or *False* according to the instructions above.

**Constraints**

The number will be between $1$ and $3999$ (both included).

**Sample Input**

	CDXXI

**Sample Output**

	True

**References**  

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is [available here](http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-13--regular-expression-matching). You could also go through the link below to read more about regular expressions in Python.  

https://developers.google.com/edu/python/regular-expressions  


**Input Format**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T08:57:24.139Z  

```py
regex_pattern = r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/validate-a-roman-number/problem)