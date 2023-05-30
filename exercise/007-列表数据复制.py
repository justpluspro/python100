"""
将一个列表的数据复制到另一个列表中。
"""

list_data = ["hello", "world"]

"""
这里涉及到了列表数据切片
list[start:end:step]

start: 表示从什么位置开始切片
end: 表示到什么位置结束切片
step: 步长多少

"""

list_data2 = list_data[:]
print(list_data2)
