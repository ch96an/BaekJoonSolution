dic, n = {-1:(0,0), 0:(0,0)}, int(input())
for i in range(1,n+1):
	k = int(input())
	dic[i] = (dic[i-1][0]+k if i == 2 else dic[i-1][1]+k, 0 if i == 1 else max(dic[i-2])+k)
print(max(dic[n]))