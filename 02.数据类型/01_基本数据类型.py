"""
Python 中的变量不需要声明，变量在使用前必须要赋值。赋值后变量才会被创建。

也支持同时为多个变量赋值.

Python 有六种标准数据类型
1. Number 数字类型
2. 字符串类型
3. List 列表
4. Tuple 元祖
5. Set 集合
6. Dictionary 字典

其中 Number 字符串以及元祖不可变，List Set 以及 Dictionary 均属于可变
"""

# 整型
age = 10
# 字符串
name = "jack"
# 浮点型
price = 100.0

print(age)
print(name)
print(price)

print("===============================")
# 一次为多个变量赋值
a = b = c = 1
print(a)
print(b)
print(c)

print("===============================")
# 一次为多个变量赋不同类型的值
d,e,f = 1,3, "张三"
print(d)
print(e)
print(f)
