"""
#10-1.py
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


print('각 원소가 속한 집합:', end =' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')

print()

print('부모 테이블:', parent)

#10-2.py
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


print('각 원소가 속한 집합:', end =' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')

print()

print('부모 테이블:', parent)

#10-4.py

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i


cycle = False


for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)


if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")      

print('각 원소가 속한 집합:', end =' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')
print()
print('부모 테이블:', parent)

#10-5.py 크루스칼 알고리즘

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i


edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

result = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

#10-6.py 위상 정렬 소스코드
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]


for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end =' ')


topology_sort()



#10-7.py
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())

parent = [0]*(n+1)
for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('Yes')
        else:
            print('No')


#10-8.py
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split())

parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

result = 0
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
"""

#10-9.py
from collections import deque
import copy


v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] ==0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()



