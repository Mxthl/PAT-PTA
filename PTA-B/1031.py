import re
N = int(raw_input())

quanzhong = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
jianyan = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6: '6', 7:'5', 8:'4', 9:'3', 10:'2'}
h = 0

for i in range(N):
	sum = 0
	w_n = raw_input()
	res = re.match('[0-9]{17}', w_n)
	if not res:
		h += 1
		print w_n
	else:
		for n in range(17):
			sum += int(w_n[n]) * quanzhong[n]
		if jianyan[sum%11] != w_n[-1]:
			h += 1
			print w_n
if h == 0:
	print 'All passed'
		
			
		