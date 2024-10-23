#9월 12일 풀이
import sys
input = sys.stdin.readline
chess = [input().strip() for _ in range(8)]
oddc = 0
evenc = 0
for i in range(0,8,2):
    for j in range(0,8,2):
        if chess[i][j] == 'F':
            oddc +=1
for n in range(1,9,2):
    for m in range(1,9,2):
        if chess[n][m] == 'F':
            evenc +=1
print(oddc+evenc)