def merge_sort(arr,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)

def merge(arr,p,q,r):
    tmp=[]
    i=p
    j=q+1
    global num2
    global answer
    while i<=q and j<=r:
        if arr[i]<=arr[j]:
           tmp.append(arr[i])
           i+=1
        else:
           tmp.append(arr[j])
           j+=1
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp.append(arr[i])
        i+=1
    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp.append(arr[j])
        j+=1
    i,t=p,0
    while i<=r:
        arr[i]=tmp[t]
        i+=1
        t+=1
        answer+=1


        if answer==num2:
            print(tmp[t-1])

import sys

answer=0
num1,num2 =  map(int,sys.stdin.readline().split())

arr1 = list(map(int,sys.stdin.readline().split()))



merge_sort(arr1,0,len(arr1)-1)

if answer<num2:
    print(-1)

