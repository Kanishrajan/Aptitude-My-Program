s=input("ENTER ")
p=''.join(c.lower() for c in s if c.isalnum())
if p==p[::-1]:
    print("YES")
else:
    print("NO")