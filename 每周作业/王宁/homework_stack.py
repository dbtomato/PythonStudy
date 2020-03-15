# 定义栈类

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


# 简单的栈测试
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

# 栈应用——检测字符串中的括号是否成对
def syntaxChecker(string):
    """检测字符串中的括号是否成对"""
    stack = Stack()
    opens = '([{'
    closes = ')]}'
    balanced = True
    for i in string:
        if i in '([{':
            stack.push(i)
        elif i in ')]}':
            if stack.is_Empty():
                balanced = False
                break
            else:
                j = stack.pop()
                if opens.find(i) != closes.find(j):
                    balanced = False
                    break
    if not stack.is_Empty():
        balanced = False
    return balanced

# 调用检测字符串括号函数
print(syntaxChecker("({])")) # True
print(syntaxChecker("{])}")) # False

# 栈应用——十进制转换为二进制
def decimal_to_bin(dec):
    """十进制转换为二进制"""
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

# 调用转换函数
print(decimal_to_bin(20)) #10100
print(decimal_to_bin(50)) # 110010
