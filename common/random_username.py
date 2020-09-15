# coding=utf-8

import random
from logging import exception

global userName, userPassword  # 为了便于后面使用，定义为全局变量
userName = ''
userPassword = ''

'''随机用户名、密码'''


def get_userNameAndPassword():
    global userName, userPassword
    # 8位用户名及6位密码
    # userName = ''.join(random.sample("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-><:}{?/", 8))
    userName = ''.join(random.sample("1234567890abcdefghijklmnopqrstuvwxyz", 8))
    return userName
    # userPassword = ''.join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.1234567890", 6))

# try:
#     get_userNameAndPassword()
#     print ("用户名:", userName)
#     print ("密码:", userPassword)
# except exception as e:
#     print(e)
