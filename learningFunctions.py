def fToC(F):
    return ((F-32) * 5) / 9
# for i in range(10, 101, 10):
#     print(fToC(i))

# if 2: then draw:
# *
# **

# if 3:
# *
# **
# ***

def drawTriangle(num):
    for i in range(1, num + 1):
        # print("*" * i)
        for j in range(i):
            print("*", end = "")
        print()

drawTriangle(5)
print()
drawTriangle(10)
