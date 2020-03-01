#!/usr/bin/env python

# -*- encoding: utf-8 -*-
# Python37-32
'''
@Author  :   {Gavin Guo}
@License :   (C) Copyright 2019-2024, {Daxiong's Company}
@Contact :   {878953027@qq.com}
@Software:   PyCharm
@File    :   LRUCache.py
@Time    :   2020/2/29 12:55
@Desc    :
'''
'''
代码引用来自：http://www.imooc.com/article/23720?block_id=tuijian_wz
'''
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = OrderedDict()

    def get(self, key):
        if key not in self.queue:
            return -1 # 要找的数据不在缓存中返回-1
        value = self.queue.pop(key) # 将命中缓存的数据移除
        self.queue[key] = value # 将命中缓存的数据重新添加到头部
        return self.queue[key]

    def put(self, key, value):
        if key in self.queue: # 如果已经在缓存中，则先移除老的数据
            self.queue.pop(key)
        elif len(self.queue.items()) == self.capacity:
            self.queue.popitem(last=False) # 如果不在缓存中并且到达最大容量，则把最后的数据淘汰
        self.queue[key] = value # 将新数据添加到头部

#测试代码
#设置一个只能放3个值得链表
testcache = LRUCache(3)
#直接把链表存满  此时的 队列由头到尾 为 3,2,1
testcache.put(1,1)
testcache.put(2,2)
testcache.put(3,3)

print("此时链表为:3,2,1 可获取到原先所有的值：")
print(testcache.get(1))
print(testcache.get(2))
print(testcache.get(3))

#尝试再插入一个新值，由于链表已满，所以剔除最先的1，若此时链表为 4,3,2
testcache.put(4,4)
print("由于链表已满，所以剔除最先的1，若此时链表为 4,3,2:")
print(testcache.get(1))
print(testcache.get(2))
print("由于获取了2一次，所以现在链表为 2,4,3")
testcache.put(5,5)
print("插入了5 ，所以3被踢出，链表尾:5,2,4")
print(testcache.get(3))

