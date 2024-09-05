#색종이
import sys
input = sys.stdin.readline
paper = [[0]*100 for _ in range(100)]
n = int(input())
for i in range(n):
    a,b = map(int,input().strip().split())
    for j in range(a, a+10):
        for k in range(b, b+10):
            if paper[j][k] == 0:
                paper[j][k] = 1
gae = 0
for m in range(100):
    gae += paper[m].count(1)
print(gae)