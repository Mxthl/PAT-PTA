n_p = int(raw_input())
rew_dic = {}
def is_prime(number):
	if number == 1:
		return False
	elif number == 2:
		return True
	else:
		for i in (2, number):
			if number % i == 0:
				return False
			else:
				return True
	
for pai in range(n_p):
	stu_num = raw_input()
	if pai == 0:
		rew_dic[stu_num] = 'Mystery Award'
	elif is_prime(pai+1):
		rew_dic[stu_num] = 'Minion'
	else:
		rew_dic[stu_num] = 'Chocolate'
		
n_c = int(raw_input())
cha_list = []
for cha in range(n_c):
	cha_n = raw_input()
	if cha_n not in rew_dic:
		print '%s: '% cha_n + 'Are you kidding?'
	elif cha_n not in cha_list:
		print'%s: '% cha_n + rew_dic[cha_n]
		cha_list.append(cha_n)
	else:
		print'%s: '% cha_n + 'Checked'
	