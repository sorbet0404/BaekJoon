#10월 23일 풀이(실2-X)
#N이 원래 수, P가 나머지
N, R = map(int, input().strip().split())
ans = 0
P = N-R
for i in range(1, int(P**(1/2)+1)):
    if P % i == 0:
        if i > R:
            ans += i
        if i*i != P and P//i>R:
            ans += P//i
print(ans)