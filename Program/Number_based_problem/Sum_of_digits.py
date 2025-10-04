n=int(input("Enter "))
t=0
num=n
while(num>0):
    t=t+num%10
    num=num//10
print(t)