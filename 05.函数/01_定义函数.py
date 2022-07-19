"""
函数的定义通过 def 关键字来进行定义
"""


# 定义函数输出 hello world
def hello():
    print("hello world")


hello()


# 定义加法函数
def sum(a, b):
    c = a + b
    return c


print(sum(10, 20))


# 定义最大值函数
def max(a, b):
    if (a < b):
        return b
    else:
        return a


print(max(19, 20))
