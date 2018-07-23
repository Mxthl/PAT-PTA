import re
n = int(raw_input())

for i in range(n):
	s = raw_input()
	r = re.search("A*PA+TA*", s)
	a = len(re.search("A*P", s).group()) - 1
	b = len(re.search("PA+T", s).group()) - 3 
	c = len(re.search("TA*", s).group()) -1
	if str(r):
		if b == 0:
			if a==c:
				print 'YES'
			else:
				print 'NO'
		else:	
			if c-a == b*a:
				print 'YES'
			else:
				print 'NO'
	else:
		print 'No'