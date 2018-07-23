N, K = [int(i) for i in raw_input().split()]

dic={}
for n in range(N):
	name, tall = [t for t in raw_input().split()]
	if name not in dic:
		dic[name] = int(tall)

pep_list = sorted(dic.items(), key=lambda x: (x[1], x[0]),reverse=True)
n_p = N / K
l_p = N-(N/K-1)*n_p
for k in range(K):
	if k == 0:
		temp_list = pep_list[0: l_p]
	else:
		temp_list = pep_list[l_p+(k-1)*n_p: l_p+(k-1)*n_p+n_p]
	res1 = temp_list[1::2]
	res = res1[::-1] + temp_list[::2]
	for n, t in res:
		print n,
	