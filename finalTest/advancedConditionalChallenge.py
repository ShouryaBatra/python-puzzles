def advanced_conditional_challenge(a, b, c):
    
    if a % 3 == 0:
        if b >=10:
            return a + b
        else:
            return a * b
    else:
        if c[0] == "A" and c[-1] == "Z":
            return abs(a - b)
        else:
            return a % b

print(advanced_conditional_challenge(12, 8, "Python"))
print(advanced_conditional_challenge(15, 2, "Awesome"))
print(advanced_conditional_challenge(17, 4, "apple"))
print(advanced_conditional_challenge(17, 4, "AsusZ"))