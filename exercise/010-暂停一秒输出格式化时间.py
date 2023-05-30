"""
暂停一秒输出，格式化当前时间
"""

import time

print(f'暂停一秒输出格式化时间: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
