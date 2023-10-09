import sys
input=sys.stdin.readline

def bellman_ford(start):
    distance, predecessor=dict(), dict()
    for node in graph:
        distance[node]=float('inf')
        predecessor[node]=None
    distance[start]=0

    for _ in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                if distance[neighbor]>distance[node]+graph[node][neighbor]:
                    distance[neighbor]=distance[node]+graph[node][neighbor]
                    predecessor[neighbor]=node
            
    for neighbor in graph[node]:
        if distance[neighbor]>distance[node]+graph[node][neighbor]:
            return -1
    
    return distance, predecessor
TC=int(input())
for _ in range(TC):
    N, M, W=map(int, input().split())
    graph={}
    for _ in range(M+1):
        S, E, T=map(int, input().split())
        if S not in graph: graph[S]={}
        graph[S][E]=T
    print(bellman_ford(1))
