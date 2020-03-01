from queue import LifoQueue


lq = LifoQueue(maxsize=0)

lq.put(0)
lq.put(1)
lq.put(2)

print(lq.queue)

lq.get()

print(lq.queue)
