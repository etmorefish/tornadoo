# -*- coding: utf-8 -*-
# @Time    : 19-11-25 下午10:37
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : test.py
# @Software: PyCharm


import  sys
from os.path import abspath, dirname
print(__file__)
print(dirname(abspath(__file__)))
root = dirname(dirname(abspath(__file__)))
print(root)
sys.path.append(root)
print(sys.path)



'''将 model 定义好，并确认在 env.py 里导入的 Base 类是在 model 定义的地方的

- 配置完成执行（ -m "注释信息"，根据情况更改，会用到生成的py文件名字里）

  > alembic revision --autogenerate -m "create_users_table"

  这里可以看到虚拟机目录在 alembic/versions 里生成了 py 文件，检查确认更新的内容，然后执行

  > alembic upgrade head

   这样就会更新 mysql 数据库了

### 命令参考

查看记录和历史

> alembic history

回退上一个升级的版本

> alembic downgrade -1

查看生成的 py 文件

> ls -l alembic/versions

其他操作

- 删除 rm alembic/versions/xxx.py 
'''