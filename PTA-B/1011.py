n = int(raw_input())
for i in range(n):
	a, b, c = [int(c) for c in raw_input().split()]
	if a + b > c:
		print 'Case #{0}: true'.format(i+1)
	else:
		print 'Case #{0}: false'.format(i+1)