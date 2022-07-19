"""
在 python 中，可以通过如下的几种方式进行类型转换
- 显示转换，只需要将数据类型作为函数名即可进行转换
int()
float()
- 隐式转换
  python 内部自动完成


以下只介绍几种常用的转换关系，其他不常用的类型需要再查
int() 强转成整型
float() 强转成浮点型
str() 强转成字符串类型


"""
num_a = 1.23
num_b = int(num_a)
# 输出 1，浮点型转 int 类型会丢失精度
print(num_b)

# bool 类型也可以进行转换
bool_a = True
int_c = int(bool_a)
print(int_c)

num_d = 1.23
num_f = 1
num_g = num_d + num_f
print(num_g)
print(type(num_g))


# 字符串和浮点数（整数）进行相加会报错，
q = "123"
w = 1
# 这行代码会报错，需要显示转换
#print(q+w)

print(int(q) + w)

a = 1.0
print(a)
print(int(a))
