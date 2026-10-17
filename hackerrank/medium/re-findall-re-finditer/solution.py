# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
s = input()

matches = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])[aeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])', s, re.IGNORECASE)

if matches:
    print(*matches, sep='\n')
else:
    print(-1)
