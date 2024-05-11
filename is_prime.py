def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

test_numbers = [5, 7, 24, 86, 97]

for num in test_numbers:
    print(f"{num} is prime: {is_prime(num)}")