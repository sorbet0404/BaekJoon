#9월 7일 풀이
import sys
input = sys.stdin.readline
A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
if A == B == C == 60:
    print("Equilateral")
if A+B+C == 180:
    if A == B or A == C or B == C:
        print("Isosceles")
    else:
        print("Scalene")
if A+B+C != 180:
    print("Error")