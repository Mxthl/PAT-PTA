good = raw_input()
bad = raw_input()
list=[]
for g in good:
	if g not in bad:
		list.append(g)
res = []		
for l in list:
	res.append(l.upper())
result = ''	
for s in res:
	if s not in result:
		result += s
		
print ''.join(result)