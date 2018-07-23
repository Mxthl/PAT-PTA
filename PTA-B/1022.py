A, B, D = [int(i) for i in raw_input().split()]
def convert_to_D(a, b, d):
	l = []
	num = a + b
	while True:
		num, remainder = divmod(num, d)
		l.append(str(remainder))
		if num == 0:
			return ''.join(l[::-1])
print convert_to_D(A, B, D)