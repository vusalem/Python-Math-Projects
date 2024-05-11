def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Write your number: "))

fact = factorial(n)

print(f"The factorial of {n} is: {fact}")
