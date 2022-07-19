"""
while condition

当 condition 条件满足的条件下，会一直循环直到满足为止

计算 1~100 的值
"""
sum = 0
i = 0
while i <= 100:
    sum += i
    # python 中不存在 i++ 这种类型的写法
    i += 1

print("1~100的和为", sum)
