#10798 세로읽기
import sys
input = sys.stdin.readline
letter=[]
chapter=''
for i in range(5):
    b = input().strip()
    b = b + '-'*(15-len(b))
    letter.append(b)
for j in range(15):
    for k in range(len(letter)):
        if letter[k][j] != '-':
            chapter+=letter[k][j]
print(chapter)