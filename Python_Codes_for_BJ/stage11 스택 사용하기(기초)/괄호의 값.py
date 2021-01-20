def check(s):
	stack = []
	match = {')':'(', ']':'['}
	for c in s:
		if c in ['(', '[']:
			stack.append(c)
		elif c in [')', ']']:
			if stack == []:
				return False
			elif stack[-1] != match[c]:
				return False
			else:
				stack.pop()
	if stack == []:
		return True
	else:
		return False

def PStype(s):
	if check(s):
		if s == '':
			return 'empty', s
		elif (s[0],s[-1]) == ('(',')') and check(s[1:-1]):
			return '()', s[1:-1]
		elif (s[0],s[-1]) == ('[',']') and check(s[1:-1]):
			return '[]', s[1:-1]
		else:
			for i in range(1,len(s)):
				if check(s[:i]):
					return '+', s[:i], s[i:]
	else:
		return False, s

def PS_to_int(s):
	typ = PStype(s)
	if typ[0] == 'empty':
		return 1
	elif typ[0] == '()':
		return 2*PS_to_int(typ[1])
	elif typ[0] == '[]':
		return 3*PS_to_int(typ[1])
	elif typ[0] == '+':
		return PS_to_int(typ[1])+PS_to_int(typ[2])
	elif typ[0] == False:
		return 0

print(PS_to_int(input()))