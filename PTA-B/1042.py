n = raw_input().lower()
dic = {}
for i in n:
	if i not in dic and i.isalpha():
		dic[i] = n.count(i)
res = sorted(dic.items(), key=lambda x: x[1], reverse=True)[0]
for r in res:
	print r,