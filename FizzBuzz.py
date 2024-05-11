def FizzBuzz():

   for i in range(1, n):
      if i % 3 == 0:
         print("Fizz")
      elif i % 5 == 0:
         print("Buzz")
      elif i % 3 == 0 and i % 5 == 0:
         print("FizzBuzz")
      else:
         print(i)
         
n = int(input(">>"))

FizzBuzz()