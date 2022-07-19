"""
list 数据类型就是写在  [] 之间，用逗号分隔的元素列表

值得注意的是: 列表中的元素类型可以不相同
同字符串一样，list 也是可以截取的
截取方式：变量[首下标：尾下标]

1. 数组也可以采用 + 号进行连接
2. list 正序遍历下标索引为 0/1/2/3/4，倒序遍历下标索引为 -1/-2/-3/-4
"""

array = ["a", 12, 123.2, True, "hello", 32, False, "987"]
print(array)

# 截取
print(array[2:5])

# 改变元素中的值
array[2:5] = [] # 将截取中的元素数组设置成空值
print(array)



array2 = ["a", 1, "b"]
array3 = ["c", 2, "d"]
print(array2 + array3)

print(array3[-1])