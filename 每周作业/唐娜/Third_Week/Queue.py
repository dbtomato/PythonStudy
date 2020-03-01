from queue import Queue, LifoQueue

# FIFO Queue
# maxsize 设置队列中数据的上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消除掉

# 新建一个队列
q = Queue(maxsize=0)

# 写入队列数据
q.put(0)
q.put(1)
q.put(2)

# 输出当前队列所有数据（打印队列里的数据）
print(q.queue)

# 删除队列数据，并返回该数据(取出队列数据）
print(q.get())


myQueue = Queue(maxsize=7)

for i in 'history':
    myQueue.put(i)

# 打印队列的数据
print(myQueue.queue)

# 取出队列中的所有数据并打印出来
while not myQueue.empty():
    print(myQueue.get())



