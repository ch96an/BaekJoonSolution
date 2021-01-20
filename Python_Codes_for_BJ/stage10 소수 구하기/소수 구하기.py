def sieve(n):
	lst = [i for i in range(2,n+1)]
	for k in lst:
		if k > 0:
			for i in range(2,n):
				p=k*i
				if p <= n:
					lst[p - 2] = 0
				else:
					break
	return [x for x in lst if x > 0]
M, N = map(int,input().split())
lst = [x for x in sieve(N) if x >= M]
for x in lst:print(x)