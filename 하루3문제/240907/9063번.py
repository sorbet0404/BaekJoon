#9월 7일 풀이
import sys
input = sys.stdin.readline
xdot=[]
ydot=[]
for i in range(int(input().strip())):
    a, b = map(int,input().strip().split())
    xdot.append(a)
    ydot.append(b)
xres = max(xdot)-min(xdot)
yres = max(ydot)-min(ydot)
if not len(xdot) == 1:
    print(xres*yres)
else:
    print(0)