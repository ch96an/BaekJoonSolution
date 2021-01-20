def sugarbags(sugar):
	bag_3 = [0,2,4,1,3][sugar%5]
	if sugar in {4,7}:
		return -1
	return bag_3 + (sugar - bag_3*3)//5

print(sugarbags(int(input())))