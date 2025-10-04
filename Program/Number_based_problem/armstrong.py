n=input("Enter ")
l,sn,num=len(n),0,int(n)
while(num>0):
    digit=num%10
    sn+=digit**l
    num=num//10
if sn==int(n):
    print("YES")
else:
    print("NO")