N = int(raw_input())
f_d = [int(f) for f in raw_input().split()]
res=[]
for day in f_d:
	temp = [t for t in f_d if t>=day]
	e = len(temp)
	if e >= day:
		res.append(day)
print max(res)