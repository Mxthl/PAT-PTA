N, e, D = [i for i in raw_input().split()]
for n in range(int(N)):
	l_list = [l for l in raw_input().split()]
	day = int(l_list[0])
	temp = l_list[1:]
	qua_pep_may = 0
	qua_pep_mus = 0
	low_day = 0
	for t in temp:
		if float(t) <float(e):
			low_day += 1 
	if low_day > round(day*1.0/2):
		qua_pep_may += 1
		if day > int(D):
			qua_pep_mus += 1
			
res_may = qua_pep_may * 100.0 / int(N)
res_mus = qua_pep_mus * 100.0 / int(N)
print '{:.1f}'.format(res_may),  '{:.1f}'.format(res_mus)