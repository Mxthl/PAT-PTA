n = raw_input()
sum = 0
dict = {'1': 'yi', '2': 'er', '3': 'san',
		'4': 'si', '5': 'wu', '6': 'liu',
		'7': 'qi', '8': 'ba', '9': 'jiu', '0': 'ling'}
for i in n:
	sum += int(i)
res = []
for s in str(sum):
	res.append(dict[s])
for r in res:
	print r,
	


