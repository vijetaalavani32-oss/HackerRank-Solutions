# Set .discard(), .remove() & .pop()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Mr. Anant Asankhya is the manager at the *INFINITE* hotel. The hotel has an infinite amount of rooms. 

One fine day, a *finite* number of tourists come to stay at the hotel. <br>
The tourists consist of:<br>
&#8594; A Captain.<br>
&#8594; An unknown group of families consisting of $K$ members per group where $K$ &#x2260; $1$.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear $K$ times per group except for the Captain's room. 

Mr. Anant needs you to help him find the Captain's room number.
<br>*The total number of tourists or the total number of groups of families is not known to you.*
<br>*You only know the value of $K$ and the room number list.*

**Input Format**

The first line consists of an integer, $K$, the size of each group.<br>
The second line contains the unordered elements of the room number list.<br>
<br>

__Constraints__

$1 < K < 1000 $

**Output Format**

Output the Captain's room number.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T08:01:46.396Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == "pop":
        s.remove(min(s))
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))




```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-the-captains-room/problem)