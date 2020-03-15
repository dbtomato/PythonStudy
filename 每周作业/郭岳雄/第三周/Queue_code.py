#!/usr/bin/env python

# -*- encoding: utf-8 -*-
# Python37-32
'''
@Author  :   {Gavin Guo}
@License :   (C) Copyright 2019-2024, {Daxiong's Company}
@Contact :   {878953027@qq.com}
@Software:   PyCharm
@File    :   Queue_code.py
@Time    :   2020/3/1 12:20
@Desc    :
'''
'''
代码引用来自：https://www.cnblogs.com/yhleng/p/9493457.html
'''

from queue import Queue,LifoQueue,PriorityQueue
from collections import deque
import time
from threading import Thread


'''
Queue 先进先出队列：
#基本FIFO队列  先进先出 FIFO即First in First Out,先进先出
#maxsize设置队列中，数据上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消掉

'''
print("----------------------------------------------------------")
q = Queue(maxsize=0)

q.put(0)
q.put(1)
q.put(2)
#输出当前队列所有数据
print(q.queue)
#获取一个值，并删除
first_value = q.get()
print(q.queue)

print(first_value)

print("----------------------------------------------------------")

#LIFO即Last in First Out,后进先出。与栈的类似，使用也很简单,maxsize用法同上
lq = LifoQueue(maxsize=0)

#队列写入数据
lq.put(0)
lq.put(1)
lq.put(2)

#输出队列所有数据
print(lq.queue)
#删除队尾数据，并返回该数据
print(lq.get())
#输出队列所有数据
print(lq.queue)

#输出:
# [0, 1, 2]
# [0, 1]

print("----------------------------------------------------------")

# 存储数据时可设置优先级的队列
# 优先级设置数越小等级越高
pq = PriorityQueue(maxsize=0)

#写入队列，设置优先级
pq.put((9,'a'))
pq.put((7,'c'))
pq.put((1,'d'))

#输出队例全部数据
print(pq.queue)

#取队例数据，可以看到，是按优先级取的。
pq.get()
pq.get()
print(pq.queue)

#输出：
[(9, 'a')]

print("----------------------------------------------------------")
#双边队列
dq = deque(['a','b'])

#增加数据到队尾
dq.append('c')
#增加数据到队左
dq.appendleft('d')

#输出队列所有数据
print(dq)
#移除队尾，并返回
print(dq.pop())
#移除队左，并返回
print(dq.popleft())
#输出:
#deque(['d', 'a', 'b', 'c'])
#c
#d
print("----------------------------------------------------------")

#生产消费模型
qq = Queue(maxsize=10)

def product(name):
    count = 1
    while True:
        q.put('步枪{}'.format(count))
        print('{}生产步枪{}支'.format(name,count))
        count+=1
        time.sleep(0.3)

def cousume(name):
    while True:
        print('{}装备了{}'.format(name,q.get()))
        time.sleep(0.3)

        q.task_done()


#部队线程
p = Thread(target=product,args=('张三',))
k = Thread(target=cousume,args=('李四',))
w = Thread(target=cousume,args=('王五',))

p.start()
k.start()
w.start()


