for _ in range(int(input())):
	k, s = input().split()
	for c in s:
		print(c*int(k), end = '')
	print('')
