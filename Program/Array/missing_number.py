n=int(input())
arr=list(map(int,input().split()))
t=n*(n+1)//2
s=sum(arr)
print("Missing Number: ",t-s)