#9월 12일 풀이
import sys
input = sys.stdin.readline
N = list(input().strip())
while len(N) != 0:
    print(*N[0:10],sep='')
    del N[0:10:1]
