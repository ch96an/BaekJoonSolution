s = input()
lst = list(map(lambda i: s.count(str(i)), range(9)))
lst[6] = int((lst[6]+s.count('9')+1)/2)
print(max(lst))