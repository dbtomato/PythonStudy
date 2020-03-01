'''
生产消费者模型
'''
import threading
import time
from queue import Queue

qq = Queue(maxsize=10)

def product(name):
    count = 1
    while True:
        qq.put('步枪{}'.format(count))
        print('{}生产步枪{}支'.format(name,count))
        count += 1
        time.sleep(0.3)


def consume(name):
    while True:
        print('{}装备了{}'.format(name, qq.get()))
        time.sleep(0.3)

        qq.task_done()


#部队线程
p = threading.Thread(target=product,args=('Jack',))
k = threading.Thread(target=consume,args=('Louis',))
w = threading.Thread(target=consume,args=('Troye',))

p.start()
k.start()
w.start()