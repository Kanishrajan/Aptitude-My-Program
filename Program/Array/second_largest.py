arr=list(map(int,input().split()))
first=second=float('-inf')
for i in arr:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
print(second)