def find_num_uppercase(string):
    upper = [chr(i) for i in range(65,91)]
    count = 0
    for letter in string:
        for capletter in upper:
            if letter == capletter:
                count += 1
    return count

print find_num_uppercase('Good MorninG!')
