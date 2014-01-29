def count_letter(string, ch):
    count=0
    for letter in string:
        if letter == ch:
            count+=1
    return count

print count_letter("Welcome", 'e')
