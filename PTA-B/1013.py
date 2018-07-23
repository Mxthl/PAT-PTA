prime_numbers = [2]
for n in range(3, 10000):
	for i in range(2, n):
		if n % i == 0:
			break
	else:
		prime_numbers.append(n)

M, N = [int(i) for i in raw_input().split()]
result = prime_numbers[M-1: N]
for c in range(len(result)):
	if (c+1) % 10 == 0:
		print result[c]
		c += 1
	else:
		print result[c],
		c += 1
	
		
		