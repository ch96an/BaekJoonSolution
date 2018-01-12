import math
solution = lambda n, k: 2*k if n <= k**2 + k else 2*k+1
for _ in range(int(input())):
	a, b = map(int,input().split())
	print(solution(b-a,int(math.sqrt(b-a-1))))