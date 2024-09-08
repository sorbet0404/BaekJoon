#9월 8일 풀이
import sys
input = sys.stdin.readline
jumsu={'A+':4.3, 'A0':4.0, 'A-':3.7,
    'B+':3.3, 'B0':3.0, 'B-': 2.7,
    'C+':2.3, 'C0': 2.0, 'C-': 1.7,
    'D+':1.3, 'D0': 1.0, 'D-': 0.7, 'F':0}
point=0
hak=0
N = int(input().strip())
for _ in range(N):
    subject, credit, record = input().strip().split()
    point+=(jumsu[record]*int(credit))
    hak+=int(credit)
print("%.2f"%(round(point/hak+10**-10,2)))