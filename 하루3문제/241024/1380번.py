#10월 24일 풀이(실5 - O)
import sys
input = sys.stdin.readline
seq=1
while 1:
    ryo = int(input())
    #학생이름 담기
    student=[]
    #순서
    number=[]
    if ryo == 0:
        break
    #출력용
    num=1
    for i in range(ryo):
        student.append(input().strip())
    for j in range(2*ryo-1):
        num, ab=input().strip().split() 
        number.append(int(num))
    set_num=list(set(number))
    set_num.sort()
    for k in set_num:
        if number.count(k) == 1:
            print(str(seq)+" "+str(student[k-1]))
            break
    seq+=1
        
    
    