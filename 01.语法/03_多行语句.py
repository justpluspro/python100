"""
Python 通常是一行写完一条语句，
如果语句很长，我们可以使用反斜杠(\)来实现多行语句
"""

a = "hello"
b = "python"
c = "world"

name = a + \
    b + \
    c

print(name)

"""
如果是在 [] {} 或者 () 中时，则不需要使用反斜杠
"""
array = ["张三", "李四", "王五",
         "赵六"]

print(array)
