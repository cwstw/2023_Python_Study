'''
Created on 2023. 7. 17.

@author: user
'''
#모듈 설치해주기
#cmd 열어서 아래 명령어 입력
#conda install cx_Oracle
import cx_Oracle

#DB 접속
con = cx_Oracle.connect('jspid/jsppw@localhost:1521/orcl')

#커서 공간 생성
cur = con.cursor()

#테이블 삭제
drop = 'drop table person'

#sql문장 실행
cur.execute(drop)

#시퀀스 삭제
dropseq = 'drop sequence perseq'
cur.execute(dropseq)

#시퀀스 생성
seq = 'create sequence perseq'
cur.execute(seq)

#테이블 생성
create = '''create table person(
            num number primary key,
            id varchar2(10),
            name varchar2(10),
            addr varchar2(10)
            )
'''
cur.execute(create)

#삽입
insert = "insert into person values(perseq.nextval, 'hong', '길동', '서울')"
cur.execute(insert)
insert = "insert into person values(perseq.nextval, 'kim', '연아', '부산')"
cur.execute(insert)
insert = "insert into person values(perseq.nextval, 'park', '지성', '제주')"
cur.execute(insert)

con.commit()

# 변수에 담지 않고 바로 작성도 가능
cur.execute('select * from person')
#반복해서 한 줄씩 출력
for row in cur :
    #튜플 형태로 출력됨
    print(row)

#수정
update = "update person set name='웬디' where id='kim'"
cur.execute(update)
con.commit()

cur.execute('select * from person')
for row in cur :
    #튜플 형태로 출력됨
    print(row)

#튜플 삭제
delete = "delete person where id = 'hong'"
cur.execute(delete)
con.commit()

cur.execute('select * from person')
for row in cur :
    #튜플 형태로 출력됨
    print(row)











