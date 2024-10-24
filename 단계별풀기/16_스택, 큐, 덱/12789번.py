#10월 24일 풀이(실3-세모)
from collections import deque
import sys
input = sys.stdin.readline
n=int(input())
park = deque()
waiting = deque(map(int,input().split()))
snack=[]
num=1
#wating이 빌 때 까지
while waiting:
    if waiting[0] == num:
        snack.append(waiting.popleft())
        num+=1
    elif park and park[0] == num:
        snack.append(park.popleft())
        num += 1
    else:
        park.appendleft(waiting.popleft())
for i in list(park):
    snack.append(park.popleft())
new_snack = sorted(snack)
if snack==new_snack:
    print("Nice")
else:
    print("Sad")