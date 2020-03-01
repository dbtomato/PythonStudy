from Third_Week.Stack import Stack

if __name__=="__main__":

    #初始化一个栈对象
    my_stack= Stack()

    my_stack.push('s')
    print("压栈:{}".format(my_stack.peek()))
    my_stack.push('w')
    print("压栈:{}".format(my_stack.peek()))
    my_stack.push('i')
    print("压栈:{}".format(my_stack.peek()))
    my_stack.push('f')
    print("压栈:{}".format(my_stack.peek()))
    my_stack.push('t')
    print("压栈:{}".format(my_stack.peek()))

    print("此时栈的大小为：{}".format(my_stack.size()),"栈顶的元素为：{}".format(my_stack.peek()))

    for i in range(0, my_stack.size()):
        print("--------------------------")
        print("出栈{}".format(my_stack.pop()))
        print("此时栈的大小为：{}".format(my_stack.size()), "栈顶的元素为：{}".format(my_stack.peek()))
        print("栈是否为空：{}".format(my_stack.is_Empty()))




