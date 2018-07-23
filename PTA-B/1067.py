rig_pas, N = [r for r in raw_input().split()]
try_tim = 0
while True:
	inp = raw_input()	

	if inp == '#':
		break
	elif inp == rig_pas and try_tim <= int(N):
		print 'Welcome in'
		break
	elif inp != rig_pas:
		try_tim += 1
		print 'Wrong password: %s' % inp
		if try_tim >= int(N):
			print 'Account locked'
			break

			
			
