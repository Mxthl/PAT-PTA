sold = list(raw_input())
want = list(raw_input())
n = len(sold)
need = 0
for w in want:
	if w not in sold:
		need += 1
	else:
		sold.remove(w)
		
if need == 0:
	print 'Yes', n-len(want)
else:
	print 'No', need


		
	