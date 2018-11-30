#!usr/bin/env python
# encoding:utf-8

"""
@author: silen
@contact: xieyangxuejun@gmail.com
@file: pracitce_mysql.py
@time: 2018/11/30 17:04
@desc: mysql数据库练习
@software: 
@license: 
"""

HOSTNAME = 'localhost'
DATABASE = 'xinhua'
USERNAME = 'web'
PASSWORD = 'web'
DB_URI = 'mysql://{}:{}@{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)

import MySQLdb
from consts import HOSTNAME, USERNAME, PASSWORD, DATABASE


def connect_mysql():
    try:
        con = MySQLdb.connect(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        print("Database version: %s" % version)
    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        exit(1)
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    connect_mysql()
