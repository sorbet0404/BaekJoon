#9월 10일 풀이 - 실버 5 - O
import sys
input = sys.stdin.readline
T = int(input().strip())
count = 0
for i in range(T):
    word = input().strip()
    group = []
    check=True
    for j in range(0,len(word)):
        if word[j] not in group:
            group.append(word[j])
        elif word[j] != word[j-1]:
            check = False
            break

    if check == True:
        count+=1
print(count)