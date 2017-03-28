#!/usr/bin/env python3

import requests

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

r = requests.get(url)

source = r.content

#print(source)

firstComment = source.find(b"<!--")

source = source[firstComment+4:]

secondComment = source.find(b"<!--")

source = source[secondComment+4:]

endComment = source.find(b"-->")

source = source[:endComment]

source = source.decode()

charString = "".join(set(source))

indexList = []
print(charString)
for k in range(0, len(charString)):
	char = charString[k]
	occurrences = source.count(char)
	print(char, ": ", occurrences)
	if occurrences == 1:
		indexList.append(source.find(char))


indexList.sort()
print(indexList)

for k in indexList:
	print(source[k])

#commentsPos = source.find(commentStr)

#print(comments)
