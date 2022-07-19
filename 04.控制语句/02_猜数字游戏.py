"""
给定一个数，和用户输入的数字进行匹配
1. 正确，提示用户猜对了
2. 错误，提示用户猜错了，并且给出大小提示
"""
target = 57
guess = -1
print('欢迎进入猜数字游戏')
while guess != target:
    guess = int(input('请输入你猜的数字'))
    if(guess == target):
        print('你真棒，猜对了')
    elif(guess < target):
        print('小啦')
    else:
        print('大啦')