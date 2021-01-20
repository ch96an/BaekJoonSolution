stack = []
pu=lambda y:stack.append(y)
po=lambda:print(stack.pop() if stack else -1)
si=lambda:print(len(stack))
em=lambda:print(0 if stack else 1)
to=lambda:print(stack[-1] if stack else -1)
dic={'pop':po,'size':si,'empty':em,'top':to}
f=lambda x:pu(x[1]) if len(x)==2 else dic[x[0]]()
for i in range(int(input())):f(input().split())