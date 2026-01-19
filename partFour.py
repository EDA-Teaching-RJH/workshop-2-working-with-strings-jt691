import random
#while (True):
secret_number = random.randint(1,10)

x = int(input("guess the number"))

if x == secret_number:
    print("correct")

elif x <= secret_number:
        print("value is higher")

elif x >= secret_number:
        print("value is lower")

print("the secret number is",secret_number)
# age = int(input("Age:"))

# if age >= 18:
#     print("You are an adult")

# elif age <= 17:
#     print("you are a child")