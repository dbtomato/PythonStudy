#!/usr/bin/env python

# -*- encoding: utf-8 -*-
# Python37-32
'''
@Author  :   {Gavin Guo}
@License :   (C) Copyright 2019-2024, {Daxiong's Company}
@Contact :   {878953027@qq.com}
@Software:   PyCharm
@File    :   Stack_code.py
@Time    :   2020/3/1 13:38
@Desc    :
'''

'''
代码引用来自：https://blog.csdn.net/qq_37941538/article/details/90138129
'''

class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_Empty(self):
        return self.items == []

    # 返回栈顶元素
    # 如果为空返回None
    def peek(self):
        if self.is_Empty():
            return None
        return self.items[len(self.items) - 1]

    # 返回栈大小
    def size(self):
        return len(self.items)

    # 压栈，添加新元素进栈
    def push(self, item):
        self.items.append(item)

    # 出栈，删除栈顶元素
    def pop(self):
        return self.items.pop()


if __name__ == "__main__":
    # 初始化一个栈对象
    my_stack = Stack()

    my_stack.push('h')
    print("压栈：{}".format(my_stack.peek()))
    my_stack.push('a')
    print("压栈：{}".format(my_stack.peek()))

    print("此时栈大小为:{}，栈顶元素为：{}".format(my_stack.size(), my_stack.peek()))
    print("出栈:{}".format(my_stack.pop()))
    print("栈是否为空:{}".format(my_stack.is_Empty()))

    print("此时栈大小为:{}，栈顶元素为：{}".format(my_stack.size(), my_stack.peek()))
    print("出栈:{}".format(my_stack.pop()))
    print("栈是否为空:{}".format(my_stack.is_Empty()))

    print("此时栈大小为:{}，栈顶元素为：{}".format(my_stack.size(), my_stack.peek()))
    print("栈是否为空:{}".format(my_stack.is_Empty()))

    """
    压栈：h
    压栈：a

    此时栈大小为:2，栈顶元素为：a
    出栈:a
    栈是否为空:False

    此时栈大小为:1，栈顶元素为：h
    出栈:h
    栈是否为空:True

    此时栈大小为:0，栈顶元素为：None
    栈是否为空:True
    """


def syntaxChecker(string):
    stack = Stack()
    opens = '([{'
    closes = ')]}'
    balanced = True
    for i in string:
        if i in '([{':
            #第一个括号无需判断优先级，直接插入
            if stack.is_Empty():
                stack.push(i)
            # 后续括号，与栈顶括号做优先级判断，只有优先级高的才能插入
            elif opens.find(i) <= opens.find(stack.peek()):
                stack.push(i)
            else:
                balanced = False
        elif i in ')]}':
            if stack.is_Empty():
                balanced = False
                break
            else:
                j = stack.pop()
                if opens.find(j) != closes.find(i):
                    balanced = False
                    break
    if not stack.is_Empty():
        balanced = False
    return balanced


print('{[()]} 的结果是：',syntaxChecker('{[()]}'))
print('([{}]) 的结果是：',syntaxChecker('([{}])'))
print('{[()()]} 的结果是：',syntaxChecker('{[()()]}'))
print('{[(]]} 的结果是：',syntaxChecker('{[(]]}'))
print('{[())) 的结果是：',syntaxChecker('{[()))'))

def decimal_to_bin(dec):
    stack = Stack()
    bin_str = ''
    if dec == 0:
        stack.push(0)
    while dec > 0:
        a = dec % 2
        stack.push(a)
        dec = int(dec / 2)
    while not stack.is_Empty():
        bin_str += str(stack.pop())
    return bin_str

print(decimal_to_bin(18))
print(decimal_to_bin(2))
print(decimal_to_bin(4))
