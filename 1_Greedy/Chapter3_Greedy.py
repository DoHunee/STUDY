"""
# 2 큰수의 법칙(1)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1


print(result)

# 큰수의 법칙 (2)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
print("count1: ",count)
print(m%(k+1))
count += m%(k+1)
print("count2: ",count)

result = 0
result += (count)*first
result += (m-count)*second

print(result)


# 숫자 카드 게임
# 3-3.py
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 3-4.py
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 1001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)


#4. 1이 될때까지
# 3-5
n, k = map(int, input().split())
result = 0

while n>k:
    while n % k !=0:
        n -= 1
        result += 1
    n //= k
    result += 1


while n >1 :
    n -= 1
    result += 1
print(result)

"""

# 3-6
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n <k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)
