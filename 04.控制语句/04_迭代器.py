"""
类似于 Java 的iterator，

同理也可以根据 for 循环进行遍历
"""

list = ["hello", "world", 1, True, 2.3]
# 获取 list 的迭代器
iter1 = iter(list)
# 输出下一个
print(next(iter1))
print(next(iter1))

