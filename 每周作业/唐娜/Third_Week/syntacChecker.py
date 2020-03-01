import string

from Third_Week.Stack import Stack
'''
首先创建一个栈对象，并新建一个包含所有左括号的数组和一个包含所有右括号的数组（注意同种括号下标需要对应），接着讲匹配状态设为True
然后对输入的字符串进行判断
如果匹配到左括号，则压栈
如果匹配到右括号
如果此时栈为空，匹配状态设为False，因为空栈缺少左括号肯定是不匹配
如果栈不为空，则出栈当前的栈顶元素，如果此时符号类型匹配，则确定是一组括号
循环直到无法匹配到括号
最后判断如果栈不为空，则匹配失败，如果匹配成功则匹配状态不做修改仍为True
返回匹配状态
————————————————
版权声明：本文为CSDN博主「薛定谔的哈士奇」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_37941538/article/details/90138129
'''
class syntaxChecker(object):


    def syntaxCheck(self,string):
        stack =Stack()
        opens='([{'
        closes=')]}'
        balanced = True
        for i in string:
            if i in '([{':
                stack.push(i)
            elif i in ')]}':
                if stack.is_Empty():
                    balanced=False
                    break
                else:
                    j=stack.pop()
                    if opens.find(i) != closes.find(j):
                        balanced=False
                        break
        if not stack.is_Empty():
            balanced=False
        return balanced

if __name__ == '__main__':
    my=syntaxChecker()

    string = '{}'
    TorF = my.syntaxCheck(string)
    print(TorF)

