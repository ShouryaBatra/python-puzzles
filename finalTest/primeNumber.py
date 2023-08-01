import math
n = int(input("enter a positive integer: "))
isPrime = True
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        isPrime = False
        break

# if n == 4 or n == 6 or n == 8:
#     isPrime = False
# if isPrime:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")



print(f"{n} is {'' if isPrime else 'not '}a prime number") 
# print(f"{n} is {isPrime ? '' : 'not '}a prime number") 