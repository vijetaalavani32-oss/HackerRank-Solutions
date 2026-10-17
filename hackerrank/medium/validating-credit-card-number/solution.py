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
