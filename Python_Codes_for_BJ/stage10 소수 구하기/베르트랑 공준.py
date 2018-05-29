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

lst = sieve(123456*2)
while True:
	n = int(input())
	if n==0:break;
	print(len([x for x in lst if n<x and x<=2*n]))
