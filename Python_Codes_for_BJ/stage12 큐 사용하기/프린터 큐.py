def printer(n,k,order):
	lst = [(order[x],False if x==k else True) for x in range(len(order))]
	flag, i = True, 0
	while flag:
		if lst[0][0] == max(lst,key=lambda x:x[0])[0]:
			flag = lst.pop(0)[1]
			i +=1
		else:
			lst.append(lst.pop(0))
	print(i)

for _ in range(int(input())):
	n,k=map(int,input().split())
	lst=list(map(int,input().split()))
	printer(n,k,lst)