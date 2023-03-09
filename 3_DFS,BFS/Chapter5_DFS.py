"""
#5-1.py
stack = []
stack.append(5)
stack.append(2)
stack.pop()
stack.append(1)

print(stack)
print(stack[::-1])

#5-2.py
from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(1)
queue.popleft()
queue.append(2)

print(queue)
queue.reverse()
print(queue)

#5-3.py
def recursive_function(i):
    print('재귀함수 호출')
    if i == 100:
        return 
    print(i, '번째 재귀함수에서', i+1,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)


def factorial_iterative(n):
    result = 1
    for i in range (1, n+1):
        print(result)
        result *= i
    return result

list = []
def factorial_recursive(n):
    print(n)
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)

print(factorial_iterative(5))

#5-6.py
INF = 99999999999999999999

praph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(praph)

#5-7.py
graph = [[]for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)


#5-8.py
def dfs(graph, v, visited):
    print('start',v, end = ' ')
    visited[v] = True
    print(visited,v, '에 해당하는',graph[v],'을 고려할거야', end = ' ')
    for i in graph[v]:
        print(i, end= ' ')
        if not visited[i]==True:
            print("번은 아직 고려 안한 애야!","|")
            dfs(graph, i, visited)
        else: print("번은 고려했어|")

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]


visited = [False]*9

dfs(graph, 1, visited)


# 5-9.py
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    print('start',queue)
    visited[start] = True
    while queue:
        print(queue,end = '는 이거고, ')
        v = queue.popleft()
        print(v, '번째 노드를 선택해.', graph[v],'들릴거야')
        for i in graph[v]:
            print("  -", i,"번 봐", end = " ")
            if not visited[i]:
                print(i,end = '번 아직 안들렸어. ')
                queue.append(i)
                visited[i]=True
                print(queue,visited,"|")
            else: print("이미 들림 |")

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]



visited = [False]*9
bfs(graph, 1, visited)

# 5-10.py
n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    #print('dfs 시작', end = ' ')
    if x <= -1 or x >=n or y <= -1 or y >= m:
        print('범위 밖이야')
        return False

    
    if graph[x][y] == 0:
        graph[x][y] = 1
        print('graph는 이래', graph,  end = ' ')
        print('상', end = ' ')
        dfs(x-1, y)
        print('좌', end = ' ')
        dfs(x, y-1)
        print('하', end = ' ')
        dfs(x+1,y)
        print('우', end = ' ')
        dfs(x, y+1)
        print('이번턴은 끝!!')
        return True
    else : print('이미 갔거나 못가')
    return False

result = 0
for i in range(n):
    for j in range(m):
        print(i,j,'로 옮겨가는중')
        if dfs(i,j) == True:
            print(i,j,'엇 얘 얼음하나다!')
            result += 1

print(result)



#5-10.py 스스로 해보기

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x<= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False

result = 0

for i in range(n):
    for j in range (m):
        if dfs(i,j) == True:
            result += 1

print(result)

#5-8.py
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end =' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)


graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False]*9
bfs(graph, 1, visited)

visited = [False]*9
dfs(graph, 1, visited)

"""
# 5-11.py
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))