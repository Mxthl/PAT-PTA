N = int(raw_input())
res=[]
n_list = [n for n in raw_input().split()]
for d_n in n_list:
	s_n = 0
	for s in d_n:
		s_n += int(s)
	if s_n not in res:
		res.append(s_n)
print len(res)
for r in sorted(res):
	print r,
		