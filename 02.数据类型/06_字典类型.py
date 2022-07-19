"""
Dictionary 是 Python 中一种非常有用的数据类型，用 {} 来标识
它是一个无序的 key:value 的键值对集合

类似于 Java 中的 map 数据类型

另外，dict 可以直接从键值对中构建字典，通过 dict() 方法来进行构造，例如以下的代码
dictMethod = dict([(1, "hello"), (2, "google"), ("china", True)])

值得注意的是：字典的 key 不允许重复
"""

dict1 = {}
dict1['one'] = 1
dict1[2] = "hello"
# output {'one': 1, 2: 'hello'}
print(dict1)

# 取出 key 为 2 类型的值
print(dict1[2])

# 获取所有的键
print(dict1.keys())
print(type(dict1.keys()))

# 输出所有的值
print(dict1.values())
print(type(dict1.values()))


dictMethod = dict([(1, "hello"), (2, "google"), ("china", True)])
print(dictMethod)