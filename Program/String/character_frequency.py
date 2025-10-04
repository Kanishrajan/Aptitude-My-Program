def character_frequency(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
s=input()
print(character_frequency(s))