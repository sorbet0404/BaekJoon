import sys
input = sys.stdin.readline
N, K = map(int,input().strip().split())
measure = []
for i in range(1,N+1):
    if N % i == 0:
        measure.append(i)
if len(measure) < K:
    print(0)
else:
    print(measure[K-1])