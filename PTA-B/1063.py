import math
N = int(raw_input())
res=0
for n in range(N):
	a, b = [int(i) for i in raw_input().split()]
	temp = math.sqrt(a**2+b**2)
	if temp > res:
		res = temp
	
print '{:.2f}'.format(res)
	
