import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
g = [[] for _ in range(n)]

for _ in range(m):
  a,b,x,y = map(int,input().split())
  a -= 1
  b -= 1
  g[a].append((b,x,y))
  g[b].append((a,-x,-y))

pos = [(0,0)]*n
visited = [False]*n

def dfs(v,x,y):
  visited[v] = True
  pos[v] = (x,y)
  for vi,xi,yi in g[v]:
    if not visited[vi]:
      dfs(vi,x+xi,y+yi)
      
dfs(0,0,0)
for i in range(n):
  if visited[i]:
    print(*pos[i])
  else:
    print("undecidable")
