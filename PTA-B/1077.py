N, M = [int(n) for n in raw_input().split()]
for n in range(N):
	temp = [int(t) for t in raw_input().split()]
	G2 = temp[0]
	res_g1 = []
	for te in temp[1:]:
		if te >= 0 and te <= M:
			res_g1.append(te)
	G1 = (sum(res_g1) - max(res_g1) - min(res_g1))*1.0/(len(res_g1)-2)
	print int(round((G1 + G2) *1.0/2))
			