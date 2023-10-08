import sys
input = sys.stdin.readline

c = [0 for i in range(9)]
c[0], c[1], c[2] = map(int, input().split())
c[3], c[4], c[5] = map(int, input().split())
c[6], c[7], c[8] = map(int, input().split())

def judge(c):

    # horizontal
    for i in (0, 3, 6):
        if c[i] == c[i+1] and c[i+2] > 9:
            return True
        if c[i] == c[i+2] and c[i+1] > 9:
            return True
        if c[i+1] == c[i+2] and c[i] > 9:
            return True

    # vertical
    for i in (0, 1, 2):
        if c[i] == c[i+3] and c[i+6] > 9:
            return True
        if c[i] == c[i+6] and c[i+3] > 9:
            return True
        if c[i+3] == c[i+6] and c[i] > 9:
            return True
    
    # diagonal
    if c[0] == c[4] and c[8] > 9:
        return True
    if c[0] == c[8] and c[4] > 9:
        return True
    if c[4] == c[8] and c[0] > 9:
        return True
    
    if c[2] == c[4] and c[6] > 9:
        return True
    if c[2] == c[6] and c[4] > 9:
        return True
    if c[4] == c[6] and c[2] > 9:
        return True

    return False

cnt = 362880  # 9!
from itertools import permutations

for seq in permutations(range(9)):
    b = [10, 11, 12, 13, 14, 15, 16, 17, 18]

    flag = False

    for i in range(9):
        b[seq[i]] = c[seq[i]]

        if judge(b):
            flag = True
            break

    if flag:
        cnt -= 1

print(cnt / 362880)
