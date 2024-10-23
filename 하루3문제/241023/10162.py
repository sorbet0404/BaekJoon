#10월 23일 풀이(브3-O)
import sys
input=sys.stdin.readline
sec = int(input())
origin_sec = sec
five = sec//300
sec %= 300
one = sec//60
sec %= 60
ten = sec//10
if ((five*300)+(one*60)+(ten*10))==origin_sec:
    print(five,one,ten)
else:
    print(-1)