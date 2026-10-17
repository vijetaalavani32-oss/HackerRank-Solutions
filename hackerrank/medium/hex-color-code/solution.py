# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import email.utils

n = int(input())
for _ in range(n):
    name, addr = input().split()
    email_addr = email.utils.parseaddr(addr)[1]
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}", email_addr):
        print(email.utils.formataddr((name, email_addr)))
