def prime(p):
    for i in range(2,p//2):
        if p%i==0:
            return 1
p=int(input("Enter"))
if prime(p)==1:
    print("It's not prime")
else:
    print("prime")