N, symbol = [i for i in raw_input().split()]

n = 0
while (n**2+2*n) * 2 + 1 < int(N):
		n += 1
		
high = n - 1
for i in range(high):
	xn_h= high - i
	res = ' '*i + symbol * (2*xn_h + 1 ) + ' '*i
	print res
print ' '*high + symbol + ' '*high
for c in range(1, high+1):
	xn_l = high - c
	res = ' '*xn_l + symbol * (2*c + 1 ) + ' '* xn_l
	print res
print int(N) - 2*high **2 - 4 * high - 1

