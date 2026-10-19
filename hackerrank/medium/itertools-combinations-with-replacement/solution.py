# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

S, K = input().split()
S = sorted(S)
K = int(K)

for i in range(1, K + 1):
    for c in combinations(S, i):
        print(''.join(c))

