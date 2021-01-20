from collections import deque
d = deque()
dic = {'size':lambda x:print(len(d)),
	   'empty':lambda x:print(0 if d else 1),
	   'front':lambda x:print(d[0] if d else -1),
	   'back':lambda x:print(d[-1] if d else -1),
	   'push_front':d.appendleft,
	   'push_back':d.append,
	   'pop_front':lambda x:print(d.popleft() if d else -1),
	   'pop_back':lambda x:print(d.pop() if d else -1)}

for _ in range(int(input())):
	x = list(input().split())
	dic[x[0]](x[-1])
