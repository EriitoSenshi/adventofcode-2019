x = 138307
y = 654505

# Part 1
increasing_digits = []
for i in range(x, y):  # Iterating through the range
    s = str(i)
    same_digits = False
    for j in range(len(s) - 1):  # Checking if the number has two adjacent digits that are the same
        if s[j] == s[j + 1]:
            same_digits = True
    if same_digits:
        increasing_digit = True
        for k in range(len(s) - 1):  # Checking if the number has digits that are not decreasing from left to right
            if int(s[k]) > int(s[k + 1]):
                increasing_digit = False
        if increasing_digit:
            increasing_digits.append(i)

print(increasing_digits)
print(len(increasing_digits))

# Part 2
correct_passwords = []
for num in increasing_digits:  # Iterating through the accepted numbers of part 1
    s = str(num)
    is_password = False
    for j in range(len(s) - 2):  # Checking if the number has groups of more than 2 adjacent digits that are the same
        if s[j] == s[j + 1] == s[j + 2]:
            s = s.replace(s[j], 'X')  # Removing these digits from the number
    for k in range(len(s) - 1):  # Checking if the number still has two adjacent digits that are the same
        if s[k] == s[k + 1] and s[k] != 'X':
            is_password = True
    if is_password:
        correct_passwords.append(num)

print(correct_passwords)
print(len(correct_passwords))
