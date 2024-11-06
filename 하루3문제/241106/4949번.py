#11월 6일 실버 4 - X
import sys
input = sys.stdin.readline
while True:
    sen = input()
    parentheses=[]
    TF = True
    if sen == ".\n":
        break
    for j in sen:
        if j == "(" or j=="[":
            parentheses.append(j)
        elif j ==")":
            if len(parentheses) != 0 and parentheses[-1] =="(":
                parentheses.pop()
            else:
                TF = False
                break
        elif j =="]":
            if len(parentheses) != 0 and parentheses[-1] =="[":
                parentheses.pop()
            else:
                TF = False
                break
    if TF == True and len(parentheses)==0:
        print("yes")
    else:
        print("no")
    