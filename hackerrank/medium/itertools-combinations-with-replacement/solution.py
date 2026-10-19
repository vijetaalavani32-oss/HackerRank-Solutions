# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
S,K=input().split()
S=sorted(S)
K=int(K)

for c in combinations_with_replacement(S,K):
    
    print(''.join(c))
