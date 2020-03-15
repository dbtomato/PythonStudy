from queue import Queue
import time
import threading

qq = Queue(maxsize=3)

def product(name):
    count = 1
    while True:
        qq.put('步枪{}'.format(count))
        print('{}生产步枪{}支'.format(name,count))
        count += 1
        time.sleep(0.3)

def cousume(name):
    while True:
        print('{}装备了{}'.format(name,qq.get()))
        time.sleep(0.3)

        qq.task_done()

p = threading.Thread(target=product,args=('张三',))
k = threading.Thread(target=cousume,args=('李四',))
w = threading.Thread(target=cousume,args=('王五',))

p.start()
k.start()
w.start()
