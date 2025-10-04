arr=list(map(int,input().split()))
max_num=min_num=arr[0]
for i in arr:
    if i<min_num:
        min_num=i
    elif i>max_num:
        max_num=i
print(max_num,min_num)