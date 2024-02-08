def insertion_sort(arr,num2):
    answer=0 #교환 횟수
    for i in range(1,len(arr),1):
        
        answer1=0
        answer2=0
        for j in range(0, i, 1):
            if arr[j] > arr[i]:
                change=arr[i]
                for k in range(i,j,-1):
                    if arr[k]!=arr[k-1]:
                        arr[k]=arr[k-1]
                        answer+=1 #교환해야된다면 answer을 1만큼 카운트

                    if answer==num2: #카운트 수가 주어진 수에 다다르면 정답 출력
                        print(f"{' '.join(map(str,arr))}")
                    
                arr[j]=change
                answer+=1

                if answer==num2: #카운트 수가 주어진 수에 다다르면 정답 출력
                    print(f"{' '.join(map(str,arr))}")
    if answer<num2:
        print("-1")


import sys

num1,num2 =  map(int,sys.stdin.readline().split())

arr1 = list(map(int,sys.stdin.readline().split()))

insertion_sort(arr1,num2)

