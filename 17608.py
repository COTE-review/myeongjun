import sys

arraynum=0
high=0
array=[]
repeat=0
answer=1

arraynum=int(sys.stdin.readline())

while repeat<arraynum:
    array.append(int(sys.stdin.readline()))
    repeat+=1

high=array.pop()
array.reverse()

for a in array:
    if a>high:
        answer+=1
        high=a

print(answer)
