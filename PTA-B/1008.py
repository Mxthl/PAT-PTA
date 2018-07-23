n, w = [int(i) for i in raw_input().split()]
list = [c for c in raw_input().split()]

if w == 0:
	res = list
else:
	while w > n:
		w = w - n
	
	res = list[-w:] + list[:n-w]
print ' '.join(res)