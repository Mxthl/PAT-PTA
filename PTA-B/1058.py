n_s, n_q = [int(n) for n in raw_input().split()]
q_dic = {}
for q in range(n_q):
	if q not in q_dic:
		q_dic[q] = []
	q_list = [q_ for q_ in raw_input()]
	q_dic[q] += q_list
	
for s in range(n_s):
	
	