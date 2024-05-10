numbers = []

n = int(input("Range input: "))
for i in range(n):
    
    number = int(input(f"{i + 1}. Enter the number: "))
    
    numbers.append(number)

result = 1  

for number  in numbers:
    result *= number


print("The product of the numbers:", result)