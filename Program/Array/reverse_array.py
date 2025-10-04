arr=list(map(int,input().split()))
left, right = 0, len(arr) - 1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)