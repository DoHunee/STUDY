"""
#6-1.py
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1 ):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)


array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right = end
    while (left <= right):
        print('시작', (start, left, right, end))
        while (left <= end and array[left] <= array[pivot]):
            left += 1
            print("왼쪽으로 한칸 더", left, right)
        while (right > start and array[right] >= array[pivot]):
            right -= 1
            print("오른쪽에서 한칸 앞으로", left, right)
        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
            print("pivot!")
        else: 
            array[left], array[right] = array[right], array[left]
            print("change")
    quick_sort(array, start, right -1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side)+[pivot] + quick_sort(right_side)


print(quick_sort(array))

#6-11.py
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
    print(i, end = ' ')

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key = lambda student: student[1])

for student in array:
    print(student[0], end = ' ')
"""

#6-12.py
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if b[i] > a[i]:
        b[i], a[i] = a[i], b[i]
    else:
        break

print(sum(a))