# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

for _ in range(n):
    uid = input()

    if (len(uid) == 10
        and len(set(uid)) == 10
        and len(re.findall(r'[A-Z]', uid)) >= 2
        and len(re.findall(r'[0-9]', uid)) >= 3
        and uid.isalnum()):
        print("Valid")
    else:
        print("Invalid")
