#Assignment: Write a Python program that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding operation on the numbers.
#Assignment: Write a Python program that generates a random number between 1 and 100. The user should guess the number, and the program should provide hints (higher or lower) until the correct number is guessed.

#Assignment 1:
number1= int(input("what is your first number? "))
number2= int(input("what is your second number? "))
while True:
    operation = input("would you like to add(+), subtract(-), multiply(*) or divide(/) these numbers? ")
    if operation=="+":
        print(number1+number2)
    elif operation=="-":
        print(number1-number2)
    elif operation=="*":
        print(number1*number2)
    elif operation=="/":
        print(f"{number1/number2:.3f}")
    else:
        print("Please insert one of the following operations: \"+, -, *, /\"") 
        continue
    break
    
#Assignment 2 FINAL:
import random

number=random.randint(0,100)
print("I have chosen a random Number between 0-100, can you guess what it is?")
guessed = set()
name = input("What's your name? ")
while True:
    guess = int(input(f"So {name}, tell me your guess: "))
    if guess in guessed: 
        print(f"YOU ALREADY TRIED THIS, ARE YOU EVEN TRYING, {name.upper()}")
    guessed.add(guess)
    difference = abs(number-guess)
    if guess < number:
        if difference >= 10:
            print ("Is your head in the sand? aim for the sky, guess much higher!")
        else:
            print("Almost there, try a tiny bit higher!")
    elif guess > number:
        if difference >= 10:
            print("You're so far away! try much lower!")
        else:
            print("So so close! Just a tiny bit lower my friend")
    else:
        print("DING DING, WINNER WINNER CHICKEN DINNER!")
        break

#Assignment 2 original solution. with break. 
# import random
# number=random.randint(0,100)
# print("I have chosen a random Number between 0-100, can you guess what it is?")
# while True:
#     guess = int(input("Tell me your guess: "))
#     if guess < number:
#         print ("try a little higher!")
#     elif guess > number:
#         print("try a little lower!")
#     else:
#         print("YOU ARE CORRECT! WINNER")
#         break

# #Assignment 2.1: solution, but without break. 
# finished = False
# while not finished:
#     guess = int(input("Tell me your guess: "))
#     if guess < number:
#         print ("try a little higher!")
#     elif guess > number:
#         print("try a little lower!")
#     else:
#         print("YOU ARE CORRECT! WINNER")
#         finished = True
        
#Assignment more clues
# guessed = set()
# while True:
#     guess = int(input("Tell me your guess: "))
#     guessed.add(guess)
#     print(f"guesses so far: {guessed}")
#     difference = abs(number-guess)
#     if guess < number:
#         if difference >= 20:
#             print ("Is your head in the sand? aim for the sky, guess much higher!")
#         else:
#             print("Almost there, try a tiny bit higher!")
#     elif guess > number:
#         if difference >= 20:
#             print("You're so far away! try much lower!")
#         else:
#             print("So so close! Just a tiny bit lower my friend")
#     else:
#         print("DING DING, WINNER WINNER CHICKEN DINNER!")
#         break
    

    
    