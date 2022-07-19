"""
集合(set)
集合的表现形式为 {“a”, "b", "c"}
1. 创建一个空的集合采用 set(), 而不是 {}, {} 是创建一个字典
2. set 可以进行集合运算
"""

address = {"beijing", "wuhan", "hunan", "anhui", "tianjin"}
print(address)
print(type(address))

# 判断元素是否在集合中
if "beijing" in address:
    print('yes!')
else:
    print('no')

# 集合运算
set1 = set('shanghai')
set2 = set('chengdu')

# 差集
set3 = set1-set2
print(set3)

# 并集
set4 = set1|set2
print(set4)

# 交集
set5 = set1&set2
print(set5)

