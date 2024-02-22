import copy

n, m, v = map(int, input().split()) # 정점수 간선수 시작번호
arr = [[] for _ in range(n+1)]      # 0번 노드는 안쓸거임

for _ in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

for i in range(n+1):
  arr[i].sort()

arr1 = copy.deepcopy(arr)

def DFS(arr,v):
    stack = [v]
    answer = [v]
    while stack:

        while stack and not arr[stack[-1]]:
            del stack[-1]              #해당 스택이 가리키는 배열이 비었다면 스택 삭제

        if not stack:  # 스택이 비어있으면 종료
            break

        a = arr[stack[-1]].pop(0)

        if a in answer:
            continue
        answer.append(a)
        stack.append(a)

    return answer
            
def BFS(arr,v):
    queue = [v]
    answer = [v]
    while queue:

        while queue and not arr[queue[0]]:
            del queue[0]              #해당 스택이 가리키는 배열이 비었다면 스택 삭제

        if not queue:  # 스택이 비어있으면 종료
            break

        a = arr[queue[0]].pop(0)

        if a in answer:
            continue
        answer.append(a)
        queue.append(a)

    return answer




print(f"{' '.join(map(str, DFS(arr,v)))}")
print(f"{' '.join(map(str, BFS(arr1,v)))}")
