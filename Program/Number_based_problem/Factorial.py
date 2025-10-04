def recursion(n):
    if n==0 or n==1:
        return 1
    return n*recursion(n-1)
n=int(input("Enter "))
print(recursion(n)) #Recursion

a=1
for i in range(n,1,-1):
    a*=i
print(a) #Loop Concept