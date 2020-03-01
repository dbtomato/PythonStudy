from queue import Queue

####先进先出队列
q=Queue(maxsize=0)

q.put(1)
q.put(2)
q.put(3)

##打印当前队列的所有数据
print(q.queue)
##出队，并且返回所有数据
q.get()
print(q.queue)