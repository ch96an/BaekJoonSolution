x,k = [1 for _ in range(10)],10**9
for _ in range(int(input())-1):
	x = [x[1]%k if i==0 else x[8]%k if i==9 else (x[i-1]+x[i+1])%k for i in range(10)]
print(sum(x[1:])%k)