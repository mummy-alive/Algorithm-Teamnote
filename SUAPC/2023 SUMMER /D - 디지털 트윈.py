import sys
input = sys.stdin.readline

N = int(input())
mac = [[] for i in range(N+1)]

for i in range(N):
    row = list(map(int, input().rstrip()))
    for j in range(N):
        if row[j] == 1:
            mac[i+1].append(j+1)
mac[1].append(1) #시작점
mac[N].append(N) #도착점

INF = sys.maxsize
dp = [[INF for i in range(N+1)] for j in range(2)]
c = [0 for i in range(N+1)]
l = [0 for i in range(N+1)]
r = [0 for i in range(N+1)]

for i in range(1, N+1):
    if mac[i]:
        l[i] = min(mac[i])
        r[i] = max(mac[i])
    else:
        c[i] = 1

dp[1][1] = r[1]

for i in range(2, N+1):
    #dp[0][i] : li에 도착하고 최소
    if c[i] == 1:
        dp[0][i] = dp[0][i-1] + 1
    elif r[i] <= l[i-1] or (c[i]==0 and c[i-1]==1):
        dp[0][i] = r[i]-l[i] + 1 + min(dp[1][i-1] + abs(r[i]-r[i-1]), dp[0][i-1] + abs(r[i]-l[i-1]))
    else:
        dp[0][i] = r[i]-l[i] + 1 + dp[1][i-1] + abs(r[i]-r[i-1])

    #dp[1][i] : ri에 도착하고 최소
    if c[i] == 1:
        dp[1][i] = dp[1][i-1] + 1
    elif r[i-1] <= l[i] or (c[i]==0 and c[i-1]==1):
        dp[1][i] = r[i]-l[i] + 1 + min(dp[0][i-1] + abs(l[i]-l[i-1]), dp[1][i-1] + abs(l[i]-r[i-1]))
    else:
        dp[1][i] = r[i]-l[i] + 1 + dp[0][i-1] + abs(l[i]-l[i-1])

    if l[i] == 0:
        l[i] = l[i-1]
    if r[i] == 0:
        r[i] = r[i-1]

print(dp[1][N] if dp[1][N] < INF else -1)
