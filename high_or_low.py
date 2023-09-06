import random
import math

def deposit():
    while True:
        amount = input("Enter the amount you want to bet: ")
        if amount.isdigit():
            amount = int(amount)
            if 10 <= amount <= 1000:
                print("You have entered into range 10 to 100.")
                return amount  
            else:
                print("Enter a valid amount within the range (10-1000).")
        else:
            print("Enter a valid numeric amount.")

def guessed_number(guess, target_number):
    difference = abs(guess-target_number)
    if difference  == 0:
        return 5
    elif difference <= 5:
        return 3
    elif difference <= 15:
         return 2
    else:
        return 1

def high_or_low(balance):
    target_number = random.randint(1, 100)
    attempts = 3  
    print("Welcome to the High or Low game! You have 3 chances to guess the number.")

    for attempt in range(attempts):
        guess = int(input(f"Attempt {attempt + 1}: Guess the number (1-100): "))

        if guess < target_number:
            print("Too low! Try guessing higher.")
        elif guess > target_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the correct number: {target_number}")
            reward = guessed_number(guess, target_number)
            reward += balance
            print(f"You earned {balance} points.")
            break
    else:
        print(f"Sorry, you've run out of chances. The correct number was {target_number}.")

    return balance

if __name__ == "__main__":
    balance = deposit()
    balance = high_or_low(balance)
    print(f"Your final balance is ${balance}")






            



                              




def deposit():
    while True:
        amount = input("Enter the amount you want to bet: ")
        if amount.isdigit():
            amount = int(amount)
            if 10 <= amount <= 1000:
                print("You have entered into range 10 to 100.")
                return amount  # Return the valid amount
            else:
                print("Enter a valid amount within the range (10-100).")
        else:
            print("Enter a valid numeric amount.")

    
