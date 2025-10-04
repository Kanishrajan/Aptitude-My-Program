arr=list(map(int,input().split()))
target=int(input())
for i, num in enumerate(arr):
        if num == target:
            print(i)