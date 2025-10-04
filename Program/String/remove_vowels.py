def remove_vowels(s):
    vowel_set="AEIOUaeiou"
    return ''.join(c for c in s if c not in vowel_set)
s=input()
print(remove_vowels(s))