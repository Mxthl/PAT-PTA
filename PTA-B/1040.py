n = raw_input()
res = 0
times = n.count('P')
if times == 0:
	print res
for i in range(times):
	p1 = n.find('P')
	if p1 != -1:
		p2 = n[p1:].find('A')
		if p2 != -1:
			p3 = n[p2:].find('T')
				if p3!= -1:
					res += 1
		
	
			
		
