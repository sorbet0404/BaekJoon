#9월 10일 풀이
#실버 5 - x
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
for i in croatia:
    word = word.replace(i,'*')
print(len(word))