def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a
def lcm(a,b):
    return abs(a*b)//gcd(a,b) if a and b else 0
a=int(input())
b=int(input())
print("LCM: ",lcm(a,b))
print("GCD: ",gcd(a,b))
