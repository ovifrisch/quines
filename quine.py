def quine():
	tab = 9
	quote = 34
	comma = 44
	l = [
		"def quine():",
		"	tab = 9",
		"	quote = 34",
		"	comma = 44",
		"	l = [",
		"	]",
		"for i in range(0, 5):",
		"	print(l[i])",
		"for element in l:",
		"	 print(chr(tab) + chr(tab) + chr(quote) + element + chr(quote) + chr(comma))",
		"for i in range(5, len(l)):",
		"	print(chr(tab) + chr(tab) + l[i])",
		"print(l[-1])",
		"quine()",
	]
	
	for i in range(0, 5):
		print(l[i])	
	for element in l:
		print(chr(tab) + chr(tab) + chr(quote) + element + chr(quote) + chr(comma))
	for i in range(5, len(l) - 1):
		print(chr(tab) + l[i])
	print(l[-1])
quine()
