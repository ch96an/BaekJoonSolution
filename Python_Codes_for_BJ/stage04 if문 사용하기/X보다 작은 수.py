_, X = map(int, input().split())
print(" ".join([str(n) for n in map(int, input().split()) if n < X]))