inp_list = [i for i in raw_input().split()]
N1, M1 = [int(n1) for n1 in inp_list[0].split('/')]
N2, M2 = [int(n2) for n2 in inp_list[1].split('/')]
K = int(inp_list[2])
N1_M1 = N1*M2*K
N2_M2 = N2*M1*K
res = []
for m in range(min(N1_M1,N2_M2)+1, max(N1_M1,N2_M2)):
	if m%K != 0 and K%m != 0:
		res.append(m)

for r in res:
	print '%d' % r/(M1*M2) +'/' +str(K)