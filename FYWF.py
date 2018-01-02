import re

print("""
---------------------
FYWF: F*CK YOUR WORD FILTER
---------------------
Bugger-up some text to bamboozle a word filter.

:zws:	Gets replaced with a unicode zero-width space "u200B"
:zwj:	Gets replaced with a unicode zero-width joiner "u200D"
:zwnj:	Gets replaced with a unicode zero-width non-joiner "u200C"
:zwnbs:	Gets replaced with a unicode zero-width no-break space "uFEFF"
:zwmix:	Gets replaced with a string of all the zero-width characters

[rev=*]	Prepend with a RIGHT-TO-LEFT OVERRIDE control character
		Reverse message
		Append with a POP DIRECTIONAL FORMATTING character
""")

def yrekcuf(match):
	return u'\u202e' + match.group(1)[::-1] + u'\u202c'

def fuckery(string):
	string = re.sub(r":zws:", u'\u200B', string, re.IGNORECASE)
	string = re.sub(r":zwj:", u'\u200D', string, re.IGNORECASE)
	string = re.sub(r":zwnj:", u'\u200C', string, re.IGNORECASE)
	string = re.sub(r":zwnbs:", u'\uFEFF', string, re.IGNORECASE)
	string = re.sub(r":zwmix:", u'\uFEFF\u200C\u200D\u200B', string, re.IGNORECASE)
	string = re.sub(r"\[rev=([^\]]+)\]", yrekcuf, string, re.IGNORECASE)
	return string

while True:
	text = input('String: ')
	text = fuckery(text)
	encoding = input('Encoding [utf8]: ')
	if(len(encoding) == 0):
		encoding = 'utf8'
	file_name = input('Save as: ')
	with open(file_name, 'w', encoding=encoding) as f:
		f.write(text)
		print("Saved as {} to {}".format(encoding, file_name))
	print('================DO ANUDDA================')
