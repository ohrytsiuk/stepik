# put your python code here
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(r'((\w+)\2{1,})', r'\2', line)
    print(new_line)

