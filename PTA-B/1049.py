N = int(raw_input())
n_list = [float(n) for n in raw_input().split()]
res = 0
for i in range(N):
	res += n_list[i] * (N-i) * (i+1)
	
print '{:.2f}'.format(res)
	
	