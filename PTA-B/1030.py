N, P = [int(n) for n in raw_input().split()]
p_n = [int(p) for p in raw_input().split()]
c_n = []
i = 0
for number in p_n:
	c_n.append(number)
	M = max(c_n)
	m = min(c_n)
	if M <= m * P:
		i += 1
	else:
		c_n.pop()
		
print i
		