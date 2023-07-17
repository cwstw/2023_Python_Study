'''
Created on 2023. 7. 17.

@author: user
'''
import cx_Oracle

#DB 접속
con = cx_Oracle.connect('jspid/jsppw@localhost:1521/orcl')

#커서 공간 생성
cur = con.cursor()

#테이블 생성
create = '''create table employee(
            num number primary key,
            id varchar2(10),
            part varchar2(10),
            position varchar2(10),
            salary number,
            )
            '''
cur.execute(create)
seq = 'create sequence empseq'
cur.execute(seq)














