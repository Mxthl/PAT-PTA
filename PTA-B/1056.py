temp = [int(t) for t in raw_input().split()]
N = temp[0]
n_list = [i for i in temp[1:]]
res = 0
for n in range(N):
	res = res + n_list[n]*10*(N-1) + sum(n_list) - n_list[n]
print res
	


