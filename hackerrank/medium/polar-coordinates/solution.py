# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(raw_input())

for _ in range(T):
    s = raw_input()
    try:
        re.compile(s)
        print "True"
    except re.error:
        print "False"



    
