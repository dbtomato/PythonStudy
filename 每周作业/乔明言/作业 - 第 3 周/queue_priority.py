from queue import PriorityQueue

pq = PriorityQueue(maxsize=0)

pq.put((9,'a'))
pq.put((7,'c'))
pq.put((1,'d'))

print(pq.queue)

pq.get()
pq.get()

print(pq.queue)