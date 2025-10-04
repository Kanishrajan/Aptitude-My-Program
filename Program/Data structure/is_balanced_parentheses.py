def is_balanced_parentheses(s):
    stack=[]
    k={'}':'{',']':'[',')':'('}
    for i in s:
        if i in k.values():
            stack.append(i)
        elif i in k.keys():
            if not stack or stack.pop()!=k[i]:
                return False
    return len(stack)==0
s=input()
print(is_balanced_parentheses(s))