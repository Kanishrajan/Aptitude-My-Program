n=int(input("Enter "))
t=1
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        t+=i
        if i!=n//i:
            t+=n//i
if t==n:
    print("True Perfect Number")
else:
    print("False")    