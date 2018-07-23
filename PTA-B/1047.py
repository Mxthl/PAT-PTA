N = int(raw_input())
dic = {}
for n in range(N):
	t_m, sco = [i for i in raw_input().split()]
	team, member = t_m.split('-')
	if team not in dic:
		dic[team] = []
	dic[team].append(int(sco))
	
res = sorted(dic.items(), key=lambda x: sum(x[1]))
print res[-1][0], sum(res[-1][1])
	