import random

print("Welcome to the random number guessing game!")
print("You will have to guess a number between 0 and 100.")
print("You will have 5 lives!")

computer_choice = random.randint(0, 100)

user_lives = 5

while user_lives !=0:
    guess = int(input("Enter your guess:"))

    if guess == computer_choice:
        print("Congratulations", guess, "is correct!")
        break
    elif guess < computer_choice:
        print("Go higher")
    elif guess > computer_choice:
        print("Go lower")    

    user_lives -= 1

if user_lives == 0:
    print("You have run out of lives. The answer was:", computer_choice)