f = lambda s: sum(map(lambda s:len(s)*(len(s)+1)//2, s.split('X')))
for _ in range(int(input())):
	print(f(input()))