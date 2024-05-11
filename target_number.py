import random


target_number = random.randint(1, 9)
for i in range(3):
    guess = int(input(">> : "))
    
    if guess == target_number:
        print("Congratulations! ")
        break
    else:
        print("Incorrect guess. Try again.")
else:
    print("Game Over.", target_number)