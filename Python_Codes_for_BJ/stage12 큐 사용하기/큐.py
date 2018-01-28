queue = []
push = lambda x:queue.append(x)
pop = lambda x:print(queue.pop(0) if queue else -1)
size = lambda x:print(len(queue))
empty = lambda x:print(0 if queue else 1)
front = lambda x:print(queue[0] if queue else -1)
back = lambda x:print(queue[-1] if queue else -1)
dic = {'push':push,'pop':pop,'size':size,
	'empty':empty,'front':front,'back':back}
for _ in range(int(input())):
	tmp = input().split()
	dic[tmp[0]](tmp[-1])