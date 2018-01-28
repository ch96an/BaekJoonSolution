def handler(n):
	type_lst, number_dic, tmp = [], {}, 1
	for i in range(n):
		cloth, cloth_type = input().split()
		if cloth_type in type_lst:
			number_dic[cloth_type] += 1
		else:
			type_lst.append(cloth_type)
			number_dic[cloth_type] = 1
	for t in type_lst:
		tmp *= number_dic[t] + 1
	return tmp - 1
for i in range(int(input())):
	print(handler(int(input())))