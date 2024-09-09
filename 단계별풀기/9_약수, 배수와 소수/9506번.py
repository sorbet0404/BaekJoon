#9월 9일 풀이
import sys
input = sys.stdin.readline
while True:
    n = int(input().strip())
    if n == -1 :
        break
    div=[]
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    div.sort()
    if sum(div) == n:
        # 원하는 형식으로 출력
        print(f"{n} = {' + '.join(map(str, div))}")
    else:
        print(f"{n} is NOT perfect.")