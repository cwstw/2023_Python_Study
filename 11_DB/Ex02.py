'''
Created on 2023. 7. 17.

@author: user
'''
import cx_Oracle

con = cx_Oracle.connect('jspid/jsppw@localhost:1521/orcl')

#cursor공간 생성
cur = con.cursor()

#없는 테이블이면 테이블을 생성
try:  
    #기존 테이블 삭제
    drop = "drop table employee"
    cur.execute(drop)
except cx_Oracle.DatabaseError :
    print('테이블이 없습니다. 테이블을 생성합니다.')
    #테이블생성
    create = '''Create table employee(
                    num       number primary key,
                    id        varchar2(15),
                    part      varchar2(15),
                    position  varchar2(15),
                    salary    number
                ) 
            '''
    cur.execute(create)

#없는 시퀀스이면 시퀀스를 생성
try :
    #기존 시퀀스 삭제
    dropsep = "drop sequence emplseq"
    cur.execute(dropsep)
except cx_Oracle.DatabaseError :
    print('시퀀스가 없습니다. 시퀀스를 생성합니다.')
    #시퀀스생성
    createseq = "create sequence emplseq"
    cur.execute(createseq)

while True:
    id = input('id입력:')
    part    = input('part 입력:')
    position= input('position 입력:')
    
    while True:
        try:
            salary = int(input('salary입력 입력:'))
        except ValueError:
            print('salary는 숫자로 입력하세요')
        else :
            break  
    
    # insert = "insert into employee(num, id, part, position, salary)  values (emplseq.nextval,'%s','%s','%s',%d)" %(id,part,position,salary) 
    # cur.execute(insert)
    # con.commit()

    #아래 방법으로도 가능
    insert = "insert into employee(num, id, part, position, salary)  values (emplseq.nextval, :1, :2, :3, :4)"
    cur.execute(insert, (id, part, position, salary))
    con.commit()
    
    retry = input('계속?')
    if retry == 'n' :
        break
    

cur.execute('select * from employee')
for row in cur :
    print(row)
    
    
print('==============================')

update_id = input('수정할 아이디 : ')
update_part = input('수정할 부서 : ')

update = 'update employee set part=',update_part,'where id=',update_id
cur.execute(update)

cur.execute('select * from employee')
for row in cur :
    print(row)
    
print('==============================')

delete_id = input('삭제할 아이디 : ')

delete = 'delete employee where id = :1'

cur.execute(delete,delete_id)
cur.execute('select * from employee')
for row in cur :
    print(row)

cur.close()
con.close()
        
# employee 테이블생성(num,id,part,position,salary)
# emplseq 시퀀스 생성
#
# id입력:kim
# part입력:영업부
# position입력:대리
# salary입력:300 문자 입력하면 숫자로 입력하세요 계속 반복(예외처리)
# 계속?y ,n:반복 빠져나가기
#
# insert
# select 


