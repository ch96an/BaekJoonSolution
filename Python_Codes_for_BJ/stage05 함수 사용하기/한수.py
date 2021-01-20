dlist = lambda lst: [lst[i+1]-lst[i] for i in range(len(lst)-1)]
listOfOneElement = lambda lst: True if lst == [] else lst == [lst[0]]*len(lst)
listIsAS = lambda lst: listOfOneElement(dlist(lst))
han = lambda n: listIsAS(list(map(int,str(n))))
i = 0
for k in range(1,int(input())+1):
	i += 1 if han(k) else 0
print(i)