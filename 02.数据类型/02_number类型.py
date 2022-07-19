"""
Number 类型包含以下几种类型
1. int 一种整数类型的 int，表示为长整型
2. float 浮点型
3. bool  布尔类型，True False
4. complex 复数类型

需要注意的是，bool 类型可以做简单的运算，True 转换成整型值就是 1 ，同理 False 则为 0
"""

a = 1
b = 1.2
c = True

print(a)
print(b)
print(c)
print(a + c)

# 使用 type() 方法可以查看具体的类型
"""
<class 'int'>
<class 'float'>
<class 'bool'>
"""
print(type(a))
print(type(b))
print(type(c))
