solution = lambda H, W, N: ((N-1)%H+1)*100+(N//H)+(1 if N%H else 0)
for _ in range(int(input())):
	H, W, N = map(int,input().split())
	print(solution(H,W,N))