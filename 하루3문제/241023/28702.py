#10월 23일 풀이(브1-X)
import sys
input = sys.stdin.readline
for i in range(3,0,-1):
    x = input().strip()
    if x not in ['Fizz','Buzz','FizzBuzz']:
        new = int(x)+i
if new%3==0 and new%5==0:
    print("FizzBuzz")
elif new%3==0 and new%5!=0:
    print("Fizz")
elif new%3!=0 and new%5==0:
    print("Buzz")
else:
    print(new)