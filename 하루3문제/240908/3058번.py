#9월 8일 브론즈 3 - O
T = int(input())
jjak=[]
for _ in range(T):
    num = list(map(int,input().split()))
    for i in num:
        if i % 2 == 0:
            jjak.append(i)
    jjak.sort()
    num=[]
    print(sum(jjak), jjak[0])
    jjak=[]