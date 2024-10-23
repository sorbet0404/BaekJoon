#9월 13일 풀이 브론즈 1 - X
import sys
input = sys.stdin.readline
#원래 수(더하기 전)
N = input().strip()
#각 자릿수를 더한 결과
res = 0
#순환 횟수
cycle = 0
#원래의 N
origin = N
#더하기 전의 숫자의 끝과 더한 결과에서의 숫자의 끝을 더한 결과
changed = ''
if int(N) < 10:
    #한자리 수면 앞에 0을 붙인다.
    N = '0'+ N
while True:
    res = int(N[0]) + int(N[-1])
    
    str_res = str(res)
    
    changed = N[-1] + str_res[-1]
    N = changed
    cycle+=1
    if int(origin) == int(changed):
        print(cycle)
        break