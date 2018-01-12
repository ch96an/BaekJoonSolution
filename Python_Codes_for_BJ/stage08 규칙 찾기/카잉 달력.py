#(n-1)%M = x - 1
#(n-1)%N = y - 1
gcd = lambda a,b: gcd(b,a%b) if b else a
def finder(M,N,x,y):
	for i in range(N//gcd(M,N)):
		if (x-1+i*M)%N==y-1:
			return x+i*M
	return -1
for _ in range(int(input())):
	M,N,x,y = map(int,input().split())
	print(finder(M,N,x,y))
