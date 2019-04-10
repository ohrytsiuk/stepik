import requests
import re

url1 = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
url2 = "https://stepic.org/media/attachments/lesson/24472/sample1.html"

urls = []
urls2 = []

answer = requests.get(url1)
for match in re.findall(r'https.*html', answer.text):
    urls.append(match)
    response = requests.get(match)
    for match2 in re.findall(r'https.*html', response.text):
        urls2.append(match2)

if url2 in urls2:
    print("Yes")
else:
    print("No")
