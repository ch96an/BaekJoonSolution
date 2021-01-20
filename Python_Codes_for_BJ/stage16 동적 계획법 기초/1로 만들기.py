n = int(input())
lst = [float('inf') for _ in range(n+1)]
lst[1] = 0
for i in range(1,n):
	if 3*i<=n:lst[3*i]=min(lst[3*i],lst[i]+1)
	if 2*i<=n:lst[2*i]=min(lst[2*i],lst[i]+1)
	lst[i+1]=min(lst[i+1],lst[i]+1)
print(lst[n])
