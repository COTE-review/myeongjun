def selection_sort(arr,num2):
    answer=0 #교환 횟수
    for i in range(len(arr) - 1,0,-1):
        max_idx = i
        
        answer1=0
        answer2=0
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        if i != max_idx: #교환해야된다면 answer을 1만큼 카운트
            answer+=1
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

        if answer==num2 and max_idx!=i: #카운트 수가 주어진 수에 다다르면 정답 출력
            answer1=arr[max_idx]
            answer2=arr[i]
            print("{0} {1}" .format(answer1,answer2))
    if answer<num2:
        print("-1")

import sys

num1,num2 =  map(int,sys.stdin.readline().split())

arr1 = list(map(int,sys.stdin.readline().split()))

selection_sort(arr1,num2)
