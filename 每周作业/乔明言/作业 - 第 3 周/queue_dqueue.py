from collections import deque

dq = deque()

dq.append('c')
dq.appendleft('d')
dq.appendleft('e')
print(dq)
print(dq.pop())
print(dq.popleft())