# -*- coding: utf-8 -*-
# @Time    : 19-11-25 下午10:37
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : 111.py
# @Software: PyCharm


import  sys
from os.path import abspath, dirname
print(__file__)
print(dirname(abspath(__file__)))
root = dirname(dirname(abspath(__file__)))
print(root)
sys.path.append(root)
print(sys.path)