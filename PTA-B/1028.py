from datetime import datetime
n = int(raw_input())
good = 0
dic = {}
today = datetime(2014, 9, 6)
for i in range(n):
	name, date = [c for c in raw_input().split()]
	y, m, d = [int(da) for da in date.split('/')]
	b = datetime(y, m, d)
	age = (today -b).days
	age_max = (today- datetime(1814,9, 6)).days
	if age >= 0 and age <= age_max:
		good += 1
		dic[name] = age
		
res_max = sorted(dic.items(), key = lambda x : x[1])[-1][0]
res_min = sorted(dic.items(), key = lambda x : x[1])[0][0]
print good, res_max, res_min
	
	