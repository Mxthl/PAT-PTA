n = int(raw_input())
dict = {}
for i in range(n):
	name, num, score = [c for c in raw_input().split()]
	dict[name] = [num, score]
	
dict_sorted = sorted(zip(dict.keys(), dict.values()),  reverse=True)
res = []
res.append(dict_sorted[0])
res.append(dict_sorted[-1])
for k, [i, j] in res:
	print k, i
	