class stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_Empty(self):
        return self.items == []

    # 返回栈顶元素
    # 如果为空则返回 None
    def peek(self):
        if self.is_Empty():
            return None
        return self.items[len(self.items) - 1]

    # 返回栈大小
    def size(self):
        return len(self.items)

    # 入栈，添加新元素进栈
    def push(self, item):
        if self.items.append(item):
            return True

    # 出栈，删除栈顶元素
    def pop(self):
        return self.items.pop()



if __name__ == "__main__":
    # 初始化一个对象
    my_stack = stack()

    my_stack.push('h')
    print("入栈：{}".format(my_stack.peek()))
    my_stack.push('a')
    print("入栈：{}".format(my_stack.peek()))

    print("此时栈大小为：{}，栈顶元素为：{}".format(my_stack.size(),my_stack.peek()))
    print("出栈：{}".format(my_stack.pop()))
    print("栈是否为空：{}".format(my_stack.is_Empty()))

    print("此时栈大小为：{}，栈顶元素为：{}".format(my_stack.size(),my_stack.peek()))
    print("出栈：{}".format(my_stack.pop()))
    print("栈是否为空：{}".format(my_stack.is_Empty()))

    print("此时栈大小为：{}，栈顶元素为：{}".format(my_stack.size(),my_stack.peek()))
    print("栈是否为空：{}".format(my_stack.is_Empty()))









