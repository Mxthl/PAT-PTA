list = [int(i) for i in raw_input().split()]
res = []
n = 0
for i in range(len(list)/2):
	res.append([])
	res[i].append(list[i+n]) 
	res[i].append(list[i+1+n])
	n += 1

result = []	
for i, j in res:
	if j == i == 0:
		result.append((0, 0))
	elif j == 0:
		i = 0
	else:
		i = i * j
		j = j - 1
		result.append((i, j))

c = []
for i, j in result:
	c.append(i)
	c.append(j)
	
for s in c:
	print s,
	