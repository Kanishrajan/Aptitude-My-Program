n=int(input("Enter"))
re_n=0
num=n
while(num>0):
    digit=num%10
    re_n=re_n*10+digit
    num=num//10
print(re_n)
