s1 = raw_input()
s2 = raw_input()
s3 = raw_input()
s4 = raw_input()
day = {'A':'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI',
		'F': 'SAT', 'G': 'SUN'}
list = []
for i in range(min(len(s1), len(s2))):
	if s1[i] == s2[i] and s1[i].isupper():
		list.append(s1[i])

for c in range(min(len(s3), len(s4))):		
	if s3[c] == s4[c] and s3[c].isalpha():
		m = c
		
d = day[list[0]]
h = ord(list[1])-55 if list[1].isalpha() else int(list[1])


print d, "{:0>2d}".format(h)+ ':'+ "{:0>2d}".format(m) 
