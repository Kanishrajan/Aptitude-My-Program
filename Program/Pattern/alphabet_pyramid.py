n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(i):
        print(chr(65+j),end='')
    for j in range(i-2,-1,-1):
        print(chr(65+j),end='')
    print()