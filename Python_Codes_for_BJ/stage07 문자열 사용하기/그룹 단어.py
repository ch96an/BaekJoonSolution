alphabet, i = 'abcdefghijklmnopqrstuvwxyz', 0
check = lambda lst: (lst == []) or lst == list(range(lst[0],lst[-1]+1))
indicesList = lambda s, c: [i for i in range(len(s)) if s[i]==c] 
group = lambda s: list(map(lambda c:check(indicesList(s,c)), alphabet))
for _ in range(int(input())):
	i += 0 if False in group(input()) else 1
print(i)