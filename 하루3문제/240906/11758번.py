import sys
input = sys.stdin.readline
xdot = []
ydot = []
for _ in range(3):
    a,b = map(int,input().strip().split())
    xdot.append(a)
    ydot.append(b)
#세점을 이용해 구하는 삼각형 넓이 공식 사용
alpha = (xdot[0]*ydot[1])+(xdot[1]*ydot[2])+(xdot[2]*ydot[0])
beta = (xdot[1]*ydot[0])+(xdot[2]*ydot[1])+(xdot[0]*ydot[2])
result = (alpha - beta)/2
if result > 0:
    print(1)
elif result == 0:
    print(0)
else:
    print(-1)