N = raw_input()
list_n = []
for n in N:
	list_n.append(n)
r = N		
if max(list_n) == min(list_n):
	print "%d - %d = 0000 " % (int(N),  int(N))
else:
	while r != '6174':
		a = ''.join(sorted(list_n, reverse=True))
		b = ''.join(sorted(list_n))
		c = int(a) - int(b)
		print '{:0>4d}'.format(int(a)) + ' - '+ '{:0>4d}'.format(int(b)) + ' = ' + '{:0>4d}'.format(c)
		another_list = []
		for cn in str(c):
			
			another_list.append(cn)
			r = ''.join(another_list)
			list_n = another_list
	
