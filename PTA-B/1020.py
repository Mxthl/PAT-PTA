n, r = [int(i) for i in raw_input().split()]
d_list = [int(d) for d in raw_input().split()]
s_list = [int(d) for d in raw_input().split()]
dict = {}
for c in range(n):
	dict[c] = []
	dict[c].append(d_list[c])
	dict[c].append(s_list[c])
sorted_price = sorted(dict.values(), key=lambda x:(x[1]*1.0/x[0]), reverse=True)
w = 0
for i in range(n):
	if r > 0:
		if r <= sorted_price[i][0]:
			w += r*(sorted_price[i][1] * 1.0/sorted_price[i][0])
			r=0
		else:
			w += sorted_price[i][1]
			r = r - sorted_price[i][0]
	else:
		break
	
print "{:.2f}".format(w)