N = int(raw_input())
win_j = []
win_y = []
win_n_j = 0
ping_n_j = 0
lose_n_j = 0

for i in range(N):
	jia, yi = [c for c in raw_input().split()]
	if jia == 'C':
		if yi == 'C':
			ping_n_j += 1
		if yi == 'J':
			win_n_j += 1
			win_j.append('C')
		if yi == 'B':
			lose_n_j += 1
			win_y.append('B')
			
	if jia == 'J':
		if yi == 'C':
			lose_n_j += 1
			win_y.append('C')
		if yi == 'J':
			ping_n_j += 1
		if yi == 'B':
			win_n_j += 1
			win_j.append('J')
		
	if jia == 'B':
		if yi == 'C':
			win_n_j += 1
			win_j.append('B')
		if yi == 'J':
			lose_n_j += 1
			win_y['J']
		if yi == 'B':
			ping_n_j += 1
list=['B', 'C', 'J']
dict_j = {}
dict_y = {}
for l in list:
	
	dict_j[l] = win_j.count(l) 
	dict_y[l] = win_y.count(l)
	
j = sorted(dict_j.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
y = sorted(dict_y.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
print win_n_j, ping_n_j, lose_n_j
print lose_n_j, ping_n_j, win_n_j
print j[0][0], y[0][0]