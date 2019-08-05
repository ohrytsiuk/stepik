import requests
import re

# url = input()
url = 'http://pastebin.com/raw/hfMThaGb'

pattern = r"<a.+href\s?=\s?[\'|\"](\w+://)?(\w+[\.|\-|\d+|\w+]+)([\:|\"|\'\/])"

addresses = set()

answer = requests.get(url)

for match in re.findall(pattern, answer.text):
    addresses.add(match[1])

for addr in sorted(addresses):
    print(addr)
