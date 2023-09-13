import sys
input = sys.stdin.readline
N = int(input())
div = []
res = ''

for j in range(1, 10):
    if N%j == 0:
        div.append(j)

for i in range(0, N+1):
    Flag = False
    for d in div:
        if i == 0:
            res += str(div[0])
            Flag = True
            break
        elif i%(N/d) == 0:
            res += str(d)
            Flag = True
            break
    if not Flag:
        res += "-"

print(res)
