def bubble_sort(arr,num2):
    answer=0 #교환 횟수
    for i in range(len(arr)-1,-1,-1):
        
        answer1=0
        answer2=0
        for j in range(0, i, 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                answer+=1 #교환해야된다면 answer을 1만큼 카운트
                if answer==num2: #카운트 수가 주어진 수에 다다르면 정답 출력
                    answer1=arr[j]
                    answer2=arr[j+1]
                    print("{0} {1}" .format(answer1,answer2))
    if answer<num2:
        print("-1")


import sys

num1,num2 =  map(int,sys.stdin.readline().split())

arr1 = list(map(int,sys.stdin.readline().split()))

bubble_sort(arr1,num2)

