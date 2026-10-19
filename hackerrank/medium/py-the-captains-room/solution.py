# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
rooms = list(map(int, input().split()))

captain = (sum(set(rooms)) * K - sum(rooms)) // (K - 1)

print(captain)
