A, Da, B, Db = [i for i in raw_input().split()]
res_a = ''
for a in A:
	if a == Da:
		res_a += a
res_b = ''		
for b in B:
	if b == Db:
		res_b += b

result_A = int(res_a) if res_a else 0
result_B = int(res_b) if res_b else 0
print result_A + result_B
