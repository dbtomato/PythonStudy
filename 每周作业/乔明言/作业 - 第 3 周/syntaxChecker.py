import stack

def syntaxChecker(string):
    stack_sy = stack.stack()
    # 注意这里的 opens、closes 变量的设置，顺序均为 小括号、中括号、大括号，
    # 定义为顺序一致是为了方便的通过 下标 判断括号是否配对
    opens = "([{"
    closes = ")]}"
    balanced = True
    # 循环遍历字符串
    for i in string:
        # 如果是左括号，直接入栈
        if i in opens:
            stack_sy.push(i)
        # 如果是右括号，进入判断
        elif i in closes:
            # 判断1：栈是否为空，为空则 false
            if stack_sy.is_Empty():
                balanced = False
                break
            # 判断2：栈不为空，则取出栈顶左括号
            else:
                j = stack_sy.pop()
                # 判断3：在初始化变量 opens、closes 中查找左括号和右括号的下标，如果下标不同则说明不匹配
                if opens.find(j) != closes.find(i):
                    balanced = False
                    break
    # 遍历结束，如果栈不为空，说明左侧有多余左括号，false
    if not stack_sy.is_Empty():
        balanced = False
    return balanced

if __name__ == "__main__":
    syntax = "{{()}}{[]}("
    print("括号字符串 {} 合法校验：{}".format(syntax,syntaxChecker(syntax)))


