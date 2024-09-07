import sys
input = sys.stdin.readline
M = int(input().strip())
N = int(input().strip())
prime=[]
for i in range(M,N+1):
    cnt = 2
    if i > 1:
        while i % cnt !=0:
            cnt+=1
        if i == cnt:
            prime.append(i)
if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)