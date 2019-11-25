# -*- coding: utf-8 -*-
# @Time    : 19-11-24 下午5:15
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : auth.py
# @Software: PyCharm


from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from models.db import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True,nullable=False)
    password = Column(String(50))
    creatime = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "<User: #{}-{}>".format(self.id, self.username)




# Base.metadata.create_all()
if __name__ == '__main__':
    Base.metadata.create_all()

'''
__tablename__： 数据库中的表名
Column：    用来创建表中的字段的一个方法
Integer：     整形，映射到数据库中的int类型
String：       字符类型，映射到数据库中的varchar类型，使用时，需要提供一个字符长度
DateTime： 时间类型
'''



'''
add:
person = User(name=‘budong', password='qwe123')
session.add(person)
session.commit()

query:
rows = session.query(User).all()
rows = session.query(User).first()

update:
rows = session.query(User).filter(User.name=='budong').update({User.password:1})
session.commit()

delete:
rows = session.query(User).filter(User.username=='budong')[0]
print(rows)
session.delete(rows)
session.commit()

'''