N = int(raw_input())
sco_list = [int(s) for s in raw_input().split()]
req_list = [int(r) for r in raw_input().split()]
dic = {}
for sco in sco_list:
	if sco not in dic:
		dic[sco] = 0
	dic[sco] += 1

result = req_list[1:]	
for res in result:
	if res not in dic:
		dic[res] = 0
	print dic[res],
	