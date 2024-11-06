#11월 6일 실버 3 - X
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
a = [False,False] + [True]*(m-1)
primes=[]

for i in range(2,m+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, m+1, i):
        a[j] = False
for i in primes:
    if i >= n:
        print(i)