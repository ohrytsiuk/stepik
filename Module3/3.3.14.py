# put your python code here
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(r'(\w)(\w)(\w*)', r'\2\1\3', line)
    print(new_line)

