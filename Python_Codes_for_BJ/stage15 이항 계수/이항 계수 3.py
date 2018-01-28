def fac(n, k):
	tmp = 1
	for i in range(1, n+1):tmp=(tmp*i)%k
	return tmp
_p1 = lambda n,m,k:power(n,m//2,k)**2%k
_p2 = lambda n,m,k,x:n*x%k if m%2 else x
power = lambda n,m,k:n if m==1 else _p2(n,m,k,_p1(n,m,k))
inv = lambda n,k:power(n,k-2,k)
binom = lambda n,m,k:fac(n,k)*inv(fac(m,k)*fac(n-m,k),k)%k
n, m = map(int, input().split())
print(binom(n,m,10**9+7))