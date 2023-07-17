'''
Created on 2023. 7. 17.

@author: user
'''
# import 시 해당 문서를 통째로 가져오기 때문에 두번 출력
#이 때 불러올 문서의 출력문을 if로 감싸서 메인일 경우에만 실행되도록 구현
#as로 별칭 사용 가능
#import Ex04_Service

#from으로 가져오면 파일이름이나 볉칭 사용 없이 가능
from Ex04_Service import Service

s1 = Service('철수')
s1.show()