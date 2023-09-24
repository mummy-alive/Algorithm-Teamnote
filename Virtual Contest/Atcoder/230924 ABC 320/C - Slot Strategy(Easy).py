import sys
input = sys.stdin.readline
INF = sys.maxsize
from itertools import permutations

M = int(input())
S = [list(input()) for _ in range(3)]
ans = INF

for n in range(10):
	n = str(n)
	for order in permutations(range(3)):
		t = 0
		for Si in order:
			if not n in S[Si]:
				break
			while S[Si][t%M] != n:
				t += 1
			t += 1
		else:
			ans = min(ans, t-1)

if ans == INF:
	ans = -1
print(ans)
