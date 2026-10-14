# Set .symmetric_difference() Operation

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<img src="https://s3.amazonaws.com/hr-challenge-images/9421/1437912471-534f33cf60-AB.png" title="A^B.png" />
__.symmetric_difference()__<br>  

The *.symmetric\_difference()* operator returns a set with all the elements that are in the set and the iterable but not both.<br>
Sometimes, a `^` operator is used in place of the *.symmetric\_difference()* tool, but it only operates on the set of elements in _set_.<br>
The set is immutable to the *.symmetric\_difference()* operation (or `^` operation).

    >>> s = set("Hacker")
    >>> print s.symmetric_difference("Rank")
    set(['c', 'e', 'H', 'n', 'R', 'r'])

    >>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
    set(['c', 'e', 'H', 'n', 'R', 'r'])

    >>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
    set(['c', 'e', 'H', 'n', 'R', 'r'])

    >>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
    set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

    >>> print s.symmetric_difference({"Rank":1})
    set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

    >>> s ^ set("Rank")
    set(['c', 'e', 'H', 'n', 'R', 'r'])

---
__Task__<br>  

Students of District College have subscriptions to *English* and *French* newspapers. Some students have subscribed to *English* only, some have subscribed to *French* only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the *English* newspaper, and one set has subscribed to the *French* newspaper. Your task is to find the total number of students who have subscribed to either the *English* or the *French* newspaper but *not both*.

**Input Format**

The first line contains the number of students who have subscribed to the *English* newspaper. <br>
The second line contains the space separated list of student roll numbers who have subscribed to the *English* newspaper.<br>
The third line contains the number of students who have subscribed to the *French* newspaper. <br>
The fourth line contains the space separated list of student roll numbers who have subscribed to the *French* newspaper.

__Constraints__

$ 0 < Total \ number \ of \ students \ in \ college <1000$


**Output Format**

Output total number of students who have subscriptions to the *English* or the *French* newspaper but *not both*.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T06:20:02.216Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
english=set(map(int,input().split()))

b=int(input())
french=set(map(int,input().split()))

print(len(english.symmetric_difference(french)))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem)