tmp = input()
while len(tmp) > 10:
	print(tmp[0:10])
	tmp = tmp[10:]
print(tmp)