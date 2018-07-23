N, M = [int(n) for n in raw_input().split()]
m_list = [m for m in raw_input().split()]
num1 = 0
num2 = 0
for s in range(N):

	n_and_list = [l for l in raw_input().split()]
	temp = []
	for n_l in n_and_list[1:]:
		if n_l in m_list:
			temp.append(n_l)
	if temp: 
		num1 += 1
		num2 += len(temp)
		print '%s: ' % n_and_list[0],
		for i in temp:
			print i,
print num1, num2
		
		