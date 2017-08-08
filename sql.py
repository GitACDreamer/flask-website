# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-28 16:01:03
# @title:  create a sqlite3 table and populate ite with data

import sqlite3

with sqlite3.connect('sample.db') as conn:
    """create a new database if the database doesn't alread exist"""
    # get a cursor object used to excute SQL command
    cursor = conn.cursor()

    # create the table
    cursor.execute(
        'create table if not exists posts(title TEXT , details TEXT)')

    # insert dummy data into the table
    cursor.execute('insert into posts values("Good", "I\'m good.")')
    cursor.execute('insert into posts values("Well", "I\'m well.")')
    cursor.execute('insert into posts values("Excellent", "I\'m excellent.")')
    cursor.execute('insert into posts values("Okay", "I\'m okay.")')
    cursor.execute('insert into posts values("Shell" , "Hello from shell.")')
