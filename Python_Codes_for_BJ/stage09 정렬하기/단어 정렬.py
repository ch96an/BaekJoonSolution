dic = {i:[] for i in range(1,51)}
for i in range(int(input())):
	tmp = input()
	dic[len(tmp)].append(tmp)
for i in range(1,51):
	for x in sorted(list(set(dic[i]))):
		print(x)