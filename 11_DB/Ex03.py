'''
Created on 2023. 7. 18.

@author: user
'''
import cx_Oracle

con = cx_Oracle.connect('jspid/jsppw@localhost:1521/orcl')

#cursor공간 생성
cur = con.cursor()

cur.execute('select * from person')
for row in cur:
    print(row)

cur.execute('select * from employee')
for row in cur:
    print(row)


#테이블 조인해서 가져오기
join = 'select id, name, part, salary from employee natural join person'
cur.execute(join)
for row in cur:
    print(row)











