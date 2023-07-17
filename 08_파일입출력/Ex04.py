'''
Created on 2023. 7. 14.

@author: user
'''

# sungjuk.txt에서 읽어서
# sungjuk_write.txt에 쓰기

line = 'aa bb    cc dd'
print(line)
print(line.split())

fr = open('sungjuk.txt','r', encoding='UTF-8')
fw = open('sungjuk_write.txt','w', encoding='UTF-8')

# frpos = fr.tell()
# print('frpos:',frpos)

titleLine = fr.readline()
fw.write(titleLine)
fw.seek(fw.tell()-2)
fw.write("\t"+'합계\n')

for line in fr: # 2번째줄부터 반복
    total = 0
    # print(line.split())
    linesplit = line.split()
    fw.write(line)
    print(linesplit)
    for i in range(1,len(linesplit)) :
        total += int(linesplit[i])
    fw.seek(fw.tell()-2)   
    fw.write("\t"+str(total)+"\n")    
        
        
# fwpos = fw.tell()
# print('fwpos:',fwpos)

fr.close()
fw.close()

# sungjuk_write.txt
# 이름    국어   영어   수학   합계
# 길동    22    33    44    99
# 태연    32    44    56    132





