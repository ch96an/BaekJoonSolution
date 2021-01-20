n, lst = int(input()), list(map(int, input().split(' ')))
print("{0:.2f}".format((sum(lst) * 100) / (n * max(lst))))