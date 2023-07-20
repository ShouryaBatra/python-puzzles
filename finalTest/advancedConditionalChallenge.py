def advanced_conditional_challenge(a, b, c):
    a = int(a)
    b = int(b)
    c = str(c)
    
    if a % 3 == 0:
        if b >=10:
            print(a + b)
        else:
            print(a * b)
    else:
        if c[0] == "A" and c[-1] == "Z":
            print(abs(a - b))
        else:
            print(a % b)

advanced_conditional_challenge(12, 8, "Python")