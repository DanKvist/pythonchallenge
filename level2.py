#!/usr/bin/env python3

import requests

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

r = requests.get(url)

source = r.content

testStr = "Peter Pan"
print(testStr.find("P"))


#commentsPos = source.find(commentStr)

#print(comments)
