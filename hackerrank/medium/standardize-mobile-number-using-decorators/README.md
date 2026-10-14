# Class 2 - Find the Torsional Angle

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Let's dive into decorators! You are given $N$ mobile numbers. Sort them in ascending order then print them in the standard format shown below:<br><br>

	+91 xxxxx xxxxx

<br>The given mobile numbers may have $+91$, $91$ or $0$ written before the actual $10$ digit number. Alternatively, there may not be any prefix at all.
<br>

**Input Format**

The first line of input contains an integer $N$, the number of mobile phone numbers. <br>
$N$ lines follow each containing a mobile number.

**Output Format**

Print $N$ mobile numbers on separate lines in the required format.

**Sample Input**

	3
    07895462130
    919875641230
    9195969878
    
**Sample Output**

	+91 78954 62130
    +91 91959 69878
    +91 98756 41230
    
**Concept**

Like most other programming languages, Python has the concept of closures. Extending these closures gives us decorators, which are an invaluable asset. You can learn about decorators in 12 easy steps [here](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/).<br>
To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function.

**Input Format**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T07:13:34.846Z  

```py

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x,
                      self.y - no.y,
                      self.z - no.z)


    def dot(self, no):
        return (self.x * no.x +
                self.y * no.y +
                self.z * no.z)

    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )

        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem)