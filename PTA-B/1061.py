N, M = [int(n) for n in raw_input().split()]
sco = [int(s) for s in raw_input().split()]
ans = [int(a) for a in raw_input().split()]
for n in range(N):
	inp = [int(i) for i in raw_input().split()]
	sum = 0
	for m in range(M):
		if inp[m] == ans[m]:
			sum += sco[m]
	print sum