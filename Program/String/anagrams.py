s1=input()
s2=input()
s1=''.join(c.lower() for c in s1 if c.isalnum())
s2=''.join(c.lower() for c in s2 if c.isalnum())
if sorted(s1)==sorted(s2):
    print("YES")
else:
    print("NO")