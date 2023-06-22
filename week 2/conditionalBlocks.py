while True:

    x = int(input("write a number\n"))

    # print(x)

    if x < 0:
        print(f"{x} is negative")
    elif x < 10:
        print(f"{x} is one digit")

    else:
        print(f"{x} is a big number hehehehe")