A,B = map(int,input().split())
res = ''

while A > 0:
    r = A % B
    if r >= 10:
        res+=chr(55+r)
    else:
        res+=str(r)
    A = A//B
print(res[::-1])