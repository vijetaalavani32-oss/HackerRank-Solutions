# Validating Credit Card Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You and Fredrick are good friends. Yesterday, Fredrick received $N$ credit cards from __ABCD Bank__. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from __ABCD Bank__ has the following characteristics:  
<br>
► It must start with a $4$, $5$ or $6$.   
► It must contain exactly $16$ digits.  
► It must only consist of digits ($0$-$9$).  
► It may have digits in groups of $4$, separated by _one_ hyphen __"$ $-$ $"__.  
► It must __`NOT`__ use any other separator like '$ \ $ ' , '_', etc. <br>
► It must __`NOT`__ have $4$ or more consecutive repeated digits.    

**Examples**:  

<sub>__Valid Credit Card Numbers__</sub>  

	4253625879615786
    4424424424442444
    5122-2368-7954-3214
	
<sub>__Invalid Credit Card Numbers__</sub>  

	42536258796157867		#17 digits in card number → Invalid 
    4424444424442444		#Consecutive digits are repeating 4 or more times → Invalid
    5122-2368-7954 - 3214	#Separators other than '-' are used → Invalid
    44244x4424442444		#Contains non digit characters → Invalid
    0525362587961578		#Doesn't start with 4, 5 or 6 → Invalid

**Input Format**

The first line of input contains an integer $N$.  
The next $N$ lines contain credit card numbers.  

__Constraints__  

$ 0 < N < 100$

**Output Format**

Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T09:10:02.914Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

for _ in range(n):
    card = input()

    pattern = r'^[456]\d{15}$|^[456]\d{3}(-\d{4}){3}$'

    if re.fullmatch(pattern, card) and not re.search(r'(\d)\1{3}', card.replace('-', '')):
        print("Valid")
    else:
        print("Invalid")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/validating-credit-card-number/problem)