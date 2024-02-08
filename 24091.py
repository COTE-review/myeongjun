def quick_sort(arr,p,r):

    if p<r:
        q=partition(arr,p,r)
        quick_sort(arr,p,q-1)
        quick_sort(arr,q+1,r)

        
def partition(arr,p,r):
    global answer
    global num2
    x=arr[r]
    i=p
    for j in range(p,r+1,1):
        if arr[j]<x:
            
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            answer+=1

            
            if answer == num2:
                print(f"{' '.join(map(str,arr))}")
    if i!=r:
        arr[i],arr[r]=arr[r],arr[i]
        answer+=1
        if answer == num2:
            print(f"{' '.join(map(str,arr))}")
    return i

import sys
sys.setrecursionlimit(10**6)

num1,num2 =  map(int,sys.stdin.readline().split())

arr1 = list(map(int,sys.stdin.readline().split()))

answer=0 #교환 횟수

quick_sort(arr1,0,num1-1)


if answer < num2:
    print(-1)
