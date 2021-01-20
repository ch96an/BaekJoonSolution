def check(str):
	tmp = 0
	for c in str:
		if c == '(':
			tmp +=1
		elif c == ')':
			tmp -=1
		if tmp < 0:
			return 'NO'
	if tmp == 0:
		return 'YES'
	else:
		return 'NO'
for i in range(int(input())):
	print(check(input()))