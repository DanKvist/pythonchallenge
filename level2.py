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

charList = "".join(set(source))

print(charList)
for k in range(0, len(charList)):
	print(charList[k], ": ", source.count(charList[k]))

#commentsPos = source.find(commentStr)

#print(comments)
