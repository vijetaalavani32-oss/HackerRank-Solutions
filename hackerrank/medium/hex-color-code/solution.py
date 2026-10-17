# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())
inside = False

for _ in range(n):
    line = input()

    if '{' in line:
        inside = True
        continue

    if '}' in line:
        inside = False
        continue

    if inside:
        colors = re.findall(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?(?![0-9a-fA-F])', line)
        for color in colors:
            print(color)

