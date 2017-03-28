#!/usr/bin/env python


alphabet = "abcdefghijklmnopqrstuvwxyz"
offset = 2

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


solution = ""
for word in message:
	try:
		cipherCharNbr = alphabet.index(word)
	except ValueError:
		cipherCharNbr = -1
	if cipherCharNbr != -1:
		unCipheredChar = alphabet[(cipherCharNbr + offset) % len(alphabet)]
		solution += (unCipheredChar)
	else:
		solution += word


print(solution)


url = "www.pythonchallenge.com/pc/def/map.html"

intab  = alphabet
length = len(alphabet)
outtab = alphabet[offset:length] + alphabet[0:offset]
trantab = str.maketrans(intab, outtab)


#print(outtab)

print(url.translate(trantab))

#Solution: http://www.pythonchallenge.com/pc/def/ocr.html
