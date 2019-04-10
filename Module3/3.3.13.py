# put your python code here
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(r'[A|a]+\b', r'argh', line, 1)
    print(new_line)

