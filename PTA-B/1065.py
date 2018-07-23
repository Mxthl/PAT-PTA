N = int(raw_input())
n_d = []
for n in range(N):
	a, b = [i for i in raw_input().split()]
	n_d.append(a)
	n_d.append(b)
n_cha = int(raw_input())
cha_list = [c for c in raw_input().split()]
res = []
for ch in cha_list:
	if ch not in n_d:
		res.append(ch)
print len(res)
for r in sorted(res):
	print r,