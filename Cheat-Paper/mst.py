import sys
input=sys.stdin.readline
def union(a, b):
    a=find(a)
    b=find(b)
    if a>b: parent[a]=b
    else: parent[b]=a

def find(a):
    if a!=parent[a]: parent[a]=find(parent[a])
    return parent[a]

V, E=map(int ,input().split())

edge=[]
parent=list(range(V+1))
for _ in range(E):
    edge.append(list(map(int, input().split())))
edge.sort(key=lambda x:x[-1])

cnt=0
for a, b, w in edge:
    if find(a)!=find(b):
        union(a, b)
        cnt+=w
print(cnt)
