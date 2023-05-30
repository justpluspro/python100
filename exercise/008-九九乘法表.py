"""
输出九九乘法表
"""

for i in range(1, 10):
    print()
    for j in range(1, i+1):
        print(f'{i}*{j}={i*j}', end="\t")
