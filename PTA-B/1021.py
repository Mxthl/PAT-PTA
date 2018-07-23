n = raw_input()
n_dic = {}

for i in n:
	n_dic[i] = n.count(i)
for c in sorted(n_dic.keys()):
	print c + ':' + str(n_dic[c])
	
	
	