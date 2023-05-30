"""
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？

分析，兔子对数满足斐波那契数列
斐波那契数列
f(0) = 0
f(1) = 1
f(2) = f(1) + f(0)
f(3) = f(2) + f(1)
f(n) = f(n-1) + f(n-2)
"""


def fun(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fun(index - 2) + fun(index - 1)


if __name__ == '__main__':
    """注意，递归层次太多，执行效率会低"""
    for i in range(1, 30):
        print(f'第{i}个月的兔子对数为 {fun(i)}')
