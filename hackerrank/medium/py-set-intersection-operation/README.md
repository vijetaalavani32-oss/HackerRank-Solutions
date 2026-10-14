# Set .intersection() Operation

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<img src="https://s3.amazonaws.com/hr-challenge-images/9419/1437830945-a56a63892c-AB.png" title="A&B.png" />
__.intersection()__<br>  

The *.intersection()* operator returns the intersection of a set and the set of elements in an iterable.<br>
Sometimes, the *&* operator is used in place of the *.intersection()* operator, but it only operates on the set of elements in _set_.<br>
The set is immutable to the *.intersection()* operation (or *&* operation).

    >>> s = set("Hacker")
    >>> print s.intersection("Rank")
    set(['a', 'k'])

    >>> print s.intersection(set(['R', 'a', 'n', 'k']))
    set(['a', 'k'])

    >>> print s.intersection(['R', 'a', 'n', 'k'])
    set(['a', 'k'])

    >>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
    set([])

    >>> print s.intersection({"Rank":1})
    set([])

    >>> s & set("Rank")
    set(['a', 'k'])

---
__Task__<br>  

The students of District College have subscriptions to *English* and *French* newspapers. Some students have subscribed only to *English*, some have subscribed only to *French*, and some have subscribed to both newspapers.  


You are given two sets of student roll numbers. One set has subscribed to the *English* newspaper, one set has subscribed to the *French* newspaper. Your task is to find the total number of students who have subscribed to _both_ newspapers.

**Input Format**

The first line contains $n$, the number of students who have subscribed to the *English* newspaper. <br>
The second line contains $n$ space separated roll numbers of those students.<br>
The third line contains $b$, the number of students who have subscribed to the *French* newspaper. <br>
The fourth line contains $b$ space separated roll numbers of those students.

__Constraints__

$ 0 < Total \ number  \ of \  students \ in \ college < 1000 $

**Output Format**

Output the total number of students who have subscriptions to __both__  *English* and *French* newspapers.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T06:00:54.882Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
english=set(map(int,input().split()))

b=int(input())
french=set(map(int,input().split()))

print(len(english.intersection(french)))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-set-intersection-operation/problem)