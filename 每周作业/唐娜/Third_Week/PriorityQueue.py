'''
存储数据时可设置优先级的队列
优先级设置数值越小则等级越高
'''
from queue import PriorityQueue

pq=PriorityQueue()

# 写入队列，设置优先级
pq.put((7,'Ronaldo'))
pq.put((10,'Messi'))
pq.put((8,'better'))
pq.put((9,'than'))
pq.put((7.5,'is'))

#打印队列数据
print(pq.queue)

while not pq.empty():
    print(pq.get())

