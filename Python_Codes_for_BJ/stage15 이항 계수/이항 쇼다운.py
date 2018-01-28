def binom(n,k):
	tmp=1
	if n<2*k:
		for i in range(k+1,n+1):tmp*=i
		for i in range(1,n-k+1):tmp//=i
	else:
		for i in range(n-k+1,n+1):tmp*=i
		for i in range(1,k+1):tmp//=i
	print(tmp)
while True:
	n,k=map(int,input().split())
	if n:binom(n,k)
	else:break