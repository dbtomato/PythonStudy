'''
双边队列
'''
from collections import deque

dq = deque(['moi','toi'])

# 在队尾添加数据
dq.append('elle')

# 添加数据到队左
dq.appendleft('il')

# 输出队列所有数据
print(dq)

# 移除队尾，并返回
print(dq.pop())

# 移除队左并返回
print(dq.popleft())