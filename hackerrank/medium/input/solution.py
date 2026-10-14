# Enter your code here. Read input from STDIN. Print output to STDOU

x, y = map(int, input().split())
polynomial = input()

print(eval(polynomial) == y)
