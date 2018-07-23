N = int(raw_input())
result = ''
for n in range(N):
	temp = [t for t in raw_input().split()]
	for te in temp:
		if te[2] == 'T':
			result += str(ord(te[0]) - 64)
print result
			