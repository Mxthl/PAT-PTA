N = int(raw_input())
n_list = [int(n) for n in raw_input().split()]
res = 0
res_list = []
for i in range(N):
	temp1 = n_list[0: i]
	temp2 = n_list[i+1: N]
	if temp1:
		left = n_list[i] > max(temp1)
	else:
		left = 1
	if temp2:
		right = n_list[i] < min(temp2)
	else:
		right = 1
	if left and right:
		res_list.append(n_list[i])
		res += 1
print res
for r_l in res_list:
	print r_l,