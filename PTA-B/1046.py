N = int(raw_input())
res1 = 0
res2 = 0
for n in range(N):
	a1, a2, b1, b2 = [int(c) for c in raw_input().split()]
	if a2 == b2:
		continue
	elif a2 == a1+b1:
		res2 += 1
	elif b2 == a1+b1:
		res1 += 1
		
print res1, res2