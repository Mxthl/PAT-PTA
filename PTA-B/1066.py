M, N, A, B, h = [int(i) for i in raw_input().split()]
for row in range(M):
	temp = [int(t) for t in raw_input().split()]
	result=[]
	res=[]
	for col in temp:
		if col>=A and col<=B:
			res.append(h) 
		else:
			res.append(col)
	result.append(res)
