A, B = [i for i in raw_input().split()]
while len(A) < len(B):
	A = '0' + A
A_d = A[::-1]
B_d = B[::-1]
dic = {10:'J', 11:'Q', 12:'K'}
res=''
for c in range(len(B_d)):
	if (c+1) %2 != 0:
		temp = (int(B_d[c])+int(A_d[c]))%13
		if temp > 9:
			res += dic[temp]
		else:
			res += str(temp)
	else:
		minus = int(B_d[c]) - int(A_d[c])
		m = minus if minus >= 0 else minus +10
		res += str(m)
	
print res[::-1]
	
