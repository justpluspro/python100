"""
斐波那契数列。

斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
"""


def fun(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fun(index - 2) + fun(index - 1)


if __name__ == '__main__':
    for i in range(0, 10):
        print(fun(i))
