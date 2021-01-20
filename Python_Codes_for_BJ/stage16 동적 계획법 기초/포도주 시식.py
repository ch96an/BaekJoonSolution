f=lambda x,k:[x[1]+k,max(x[2:])+k,max(x[:2]),max(x[2:])]
n = int(input())
if n == 1:
	print(int(input()))
elif n == 2:
	print(int(input())+int(input()))
else:
	tmp0, tmp1 = int(input()), int(input())
	x = [tmp0+tmp1, tmp1, tmp0, 0]
	for i in range(2,n):
		x = f(x,int(input()))
	print(max(x))