"""
元祖类型采用 () 包裹，中间采用 , 进行分割。
与 list 不同的是，元祖类型中间的数值不允许更改

1.元素类型也是可以有多种类型，也可以采用 + 进行元祖连接
2.元祖中如果只有一个元素，则需要在元素后面加上 , 例如 (1,)
(1,) (1) 这两种类型是不一样的
第一个类型为元祖，第二个类型为 int

<class 'tuple'>
<class 'int'>

"""

array = ("a", True, 1, 2.3)
print(array)
print(type(array))

array2 = ("a", True)
array3 = ("b", 1.2)
print(array2 + array3)

# 元祖类型的修改是非法的，下面这段代码会报错
# array3[0] = 11
# print(array3[0])

tup = (1,)
tup2 = ("ab")
print(tup)
print(type(tup))
print(type(tup2))

