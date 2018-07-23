list = [i for i in raw_input().split()]
n_string = ''
for i in range(10):
	n_string += int(list[i])*str(i)

for s in range(len(n_string)):
	if n_string[s] != '0':
		result = n_string[s] + n_string[:s] + n_string[s+1:]
		break
print result
		

	