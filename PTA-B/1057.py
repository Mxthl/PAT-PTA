n = raw_input()
res = 0
for i in n.lower():
	if i.isalpha():
		res += (ord(i) - 96)
		
bin = []
while res!=0:
	res, remainder = divmod(res, 2)
	bin.append(str(remainder))

print bin.count('0'), bin.count('1')
	 