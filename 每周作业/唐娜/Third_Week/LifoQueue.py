
'''
LIFO:LAST IN FIRST OUT QUEUE
后进先出队列 LifoQueue,与栈类似
'''
from queue import LifoQueue

lifoq = LifoQueue()

# 队列写入数据
for i in 'lastTime':
    lifoq.put(i)

print(lifoq.queue)

# 取出所有数据并打印(倒序）
size = lifoq.qsize()
for i in range(0,size):
    if not lifoq.empty():
        print(lifoq.get())
