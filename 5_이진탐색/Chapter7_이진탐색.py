"""
def sequential_search(n, target, array):
    for i in range(n):
        if array[i]==target:
            return i+1


input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2 # 몫

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)

    else :
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None :
    print("no 원소")
else:
    print(result +1)

#7-5.py
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
        
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None :
    print("no 원소")
else:
    print(result +1)


#7-6.py
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None


n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes')
    else:
        print('no')

#7-7.py
n = int(input())
array = set(list(map(int, input().split())))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes')
    else:
        print('no')

"""
