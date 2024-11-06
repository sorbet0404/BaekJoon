#11월 6일 실버 4 - △
import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().strip().split()))
m = int(input())
mum = list(map(int,input().strip().split()))
c_num = Counter(num)
for i in mum:
    if i in c_num:
        print(c_num[i],end=' ')
    else:
        print(0,end=' ')
    