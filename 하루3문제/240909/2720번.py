#9월 9일 풀이
import sys
input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    money = int(input().strip())
    q,d,n,p = 0,0,0,0
    #쿼터용
    q += money / 25
    money = money%25
    #다임용
    d += money / 10
    money = money%10
    #니켈용
    n += money / 5
    money = money%5
    #페니용
    p += money / 1
    print(int(q),int(d),int(n),int(p))