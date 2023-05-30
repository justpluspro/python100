"""
输入三个整数x,y,z，请把这三个数由小到大输出。
"""

# x = int(input('请输入x:'))
# y = int(input('请输入y:'))
# z = int(input('请输入z:'))
#
# list_data = list()
# list_data.append(x)
# list_data.append(y)
# list_data.append(z)

list_data = list()
for i in range(0, 3):
    number = int(input('请输入:'))
    list_data.append(number)

list_data.sort()
print(list_data)
