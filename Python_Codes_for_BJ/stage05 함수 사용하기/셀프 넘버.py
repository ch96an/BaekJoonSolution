d = lambda x: x+sum(map(int,str(x)))
dic = {x:True for x in range(1,10050)}
for i in range(1,10001):
	dic[d(i)]=False
for i in range(1,10001):
	if dic[i]==True:print(i)