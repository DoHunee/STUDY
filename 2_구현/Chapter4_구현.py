"""

#4-1
n = int(input()) #int(input()) 중요!
plans = input().split()
x, y = 1, 1

# L,R,U,D

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']


for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    x, y = nx, ny


print(x,y) 

# 시간 3 체크 4-2.py
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)

# 나이트 위치 가지수
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-2,1), (2,-1), (2,1), (1,-2), (1,2), (-1,-2), (-1,2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]

    if next_row >= 1 and next_row <=8 and next_col >=1 and next_col <=8:
        result += 1

print(result)
"""

