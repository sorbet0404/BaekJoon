N,B = input().split()
N = ''.join(reversed(N))
B = int(B)

sum=0

letter = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(N)-1, -1, -1):
    sum+=letter.index(N[i])*(B**i)
print(sum)