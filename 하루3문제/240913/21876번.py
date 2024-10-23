#9월 13일 풀이 브론즈 2 - O
import sys
input = sys.stdin.readline
N = int(input().strip())
letter=['J','A','V']
S = input().strip()
for i in letter:
    S=S.replace(i,'')
if len(S) == 0:
    print("nojava")
else:
    print(S)