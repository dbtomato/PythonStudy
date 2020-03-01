from Third_Week.Stack import Stack
'''
首先创建一个栈对象，和一个存储二进制数的字符串，函数传入待转换的十进制数
提前判断该数是不是0，如果是0则直接压栈0
非零则开始执行转换操作
将十进制数%2后的结果压入栈
然后将十进制数/2得到新的数
如此循环直到所得十进制数小于一
注意这个过程中为了避免小数所以执行了强制类型转换
循环结束后如果栈不为空，则将之前压栈的元素全部按顺序出栈组成一个二进制的字符串，返回之
————————————————
版权声明：本文为CSDN博主「薛定谔的哈士奇」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_37941538/article/details/90138129
'''

class DecimalToBinary(object):
    def decimal_to_binary(self, dec):
        stack = Stack()
        bin_str = ''
        if dec == 0:
            stack.push(0)
        while dec>0:
            a = dec % 2
            stack.push(a)
            dec = int(dec / 2)
        while not stack.is_Empty():
            bin_str += str(stack.pop())
        return bin_str



if __name__ == '__main__':
    test = DecimalToBinary()
    print(test.decimal_to_binary(12))