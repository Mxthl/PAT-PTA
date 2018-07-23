N = int(raw_input())
dic = {}
for n in range(N):
	kh, jh, zh = [i for i in raw_input().split()]
	dic[jh] = [kh, zh]
	
late_n = int(raw_input())
late_list = [l for l in raw_input().split()]
for l_n in range(late_n):
	res = dic[late_list[l_n]]
	for k in res:
		print k,
	print ''

	
