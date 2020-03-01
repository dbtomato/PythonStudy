import stack

def decimal_to_bin(dec):
    stack_dtb = stack.stack()
    bin_str = ""

    if dec == 0:
        stack_dtb.push(0)

    while dec > 0:
        a = dec % 2
        stack_dtb.push(a)
        dec = dec // 2

    while not stack_dtb.is_Empty():
        bin_str += str(stack_dtb.pop())
    return bin_str

if __name__ == "__main__":
    dec = 11
    print("十进制数 {}转换为二进制等于：{}".format(dec,decimal_to_bin(dec)))