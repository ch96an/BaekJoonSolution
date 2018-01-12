mean = lambda lst: sum(lst)/len(lst)
overmean = lambda lst: [x for x in lst if x > mean(lst)]
rate = lambda lst: len(overmean(lst))*100/len(lst)

for i in range(int(input())):
	tmp = list(map(int, input().split()))
	print("{0:.3f}%".format(rate(tmp[1:])))