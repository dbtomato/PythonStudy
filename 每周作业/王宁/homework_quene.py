"""
Python四种类型的队例：
Queue：FIFO 即first in first out 先进先出
LifoQueue：LIFO 即last in first out 后进先出
PriorityQueue：优先队列，级别越低，越优先
deque:双边队列
"""

# 导入三种队列，包
from queue import Queue, LifoQueue, PriorityQueue
# 这个是双边队列的包
from collections import deque
# 导入生产者消费者模型需要的线程和时间 包
import threading
import time

# 第一种 先进先出队列
# 基本FIFO队列  先进先出 FIFO即First in First Out,先进先出
# maxsize设置队列中，数据上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消掉
q = Queue(maxsize=0)

# 写入队列数据
q.put(0)
q.put(1)
q.put(2)

# 输出当前队列所有数据
print(q.queue)
# 执行结果：deque([0, 1, 2])

# 删除队列数据，并返回该数据
print(q.get())
# 执行结果：0

# 输也所有队列数据
print(q.queue)
# 执行结果：deque([1, 2])


# 第二种 后进先出队列
# LIFO 即Last in First Out,后进先出。与栈的类似，使用也很简单,maxsize用法同上
lq = LifoQueue(maxsize=0)

# 队列写入数据
lq.put(0)
lq.put(1)
lq.put(2)

# 输出队列所有数据
print(lq.queue)
# 执行结果：[0, 1, 2]

# 删除队尾数据，并返回该数据
print(lq.get())
# 执行结果：2

# 输出队列所有数据
print(lq.queue)
# 执行结果：[0, 1]


# 第三种：优先队列
# 存储数据时可设置优先级的队列
# 优先级设置数越小等级越高
pq = PriorityQueue(maxsize=0)

# 写入队列，设置优先级
pq.put((9, 'a'))
pq.put((7, 'c'))
pq.put((1, 'd'))

# 输出队例全部数据，这个队列貌似没有什么顺序
print(pq.queue)
# 执行结果：[(1, 'd'), (9, 'a'), (7, 'c')]

# 取队例数据，可以看到，是按优先级取的。优先级越高，越先出来。
print(pq.get())
# 执行结果：(1, 'd')
print(pq.get())
# 执行结果：(7, 'c')
print(pq.queue)
# 执行结果：[(9, 'a')]


# 第四种 双边队列
# 双边队列
dq = deque(['a', 'b'])

# 增加数据到队尾
dq.append('c')
# 增加数据到队左
dq.appendleft('d')

# 输出队列所有数据
print(dq)
# 执行结果：deque(['d', 'a', 'b', 'c'])
# 移除队尾，并返回
print(dq.pop())
# 执行结果：c

# 移除队左，并返回
print(dq.popleft())
# 执行结果：d

# 输出队列所有数据
print(dq)
# 执行结果：deque(['a', 'b'])

# 综合：
# 生产消费模型
# 先进先出队列
qq = Queue(maxsize=10)


def product(name):
    """生产者函数"""
    count = 1
    while True:
        q.put('步枪{}'.format(count))
        print('{}生产步枪{}支'.format(name, count))
        count += 1
        time.sleep(0.3)


def cousume(name):
    """消费者函数"""
    while True:
        print('{}装备了{}'.format(name, q.get()))
        time.sleep(0.3)

        q.task_done()


# 部队线程，张三生产，李四和王五消费
p = threading.Thread(target=product, args=('张三',))
k = threading.Thread(target=cousume, args=('李四',))
w = threading.Thread(target=cousume, args=('王五',))

p.start()
k.start()
w.start()
