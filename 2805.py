import sys

num1,num2 =  map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

def binary_search(target, data):
    start = 0
    end = max(arr)
    while start <= end:
        mid = (start + end) // 2  #자를 높이
        answer = sum(a - mid if a > mid else 0 for a in arr)

        
        if answer == target:
            return mid
        
        elif answer > target:
            start = mid+1
            
            
        elif answer < target:
            end = mid-1
            mid = mid-1

    return mid


    

print(binary_search(num2, arr))


16.3
16 16
16
