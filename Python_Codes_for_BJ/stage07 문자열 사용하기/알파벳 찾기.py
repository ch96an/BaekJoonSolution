s, x =input(), list(range(97,123))
print(" ".join(list(map(lambda x: str(s.index(chr(x)) if chr(x) in s else -1), x))))