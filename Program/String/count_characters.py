def count_characters(s):
    vowels = consonants = digits = special = 0
    vowels_set = "aeiouAEIOU"
    for char in s:
        if char.isalpha():
            if char in vowels_set:
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1
    return vowels, consonants, digits, special
s=input()
print(count_characters(s))