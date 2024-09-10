#9월 10일
import sys
input = sys.stdin.readline
tri = list(map(int,input().strip().split()))
tri.sort()
if tri[0]+tri[1] <= tri[2]:
    print(tri[0]+tri[1]+(tri[0]+tri[1]-1))
else:
    print(tri[0]+tri[1]+tri[2])