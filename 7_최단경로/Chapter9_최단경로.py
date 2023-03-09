"""
#9-2.py

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
print(graph)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                print(i,'th graph',distance)
                print(q)

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


#9-3.py
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]


for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
print(graph)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

print(graph)


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
print(graph)

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end = " ")
        else:
            print(graph[a][b], end = " ")

    print()


#9-4.py
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


x, k = map(int, input().split())
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k] +graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)




# 9-5.py
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start]=0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0
print(distance)
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count -1, max_distance)
print(graph)
"""

