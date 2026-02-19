import random
import string
import time
from datetime import datetime

# ===============================
# 1. Guessing Game
# ===============================
def guessing_game():
    num = random.randint(1, 20)
    print("\n🎯 Guess number between 1 to 20")

    while True:
        guess = int(input("Enter guess: "))

        if guess == num:
            print("🎉 Correct!")
            break
        elif guess < num:
            print("Too Low!")
        else:
            print("Too High!")


# ===============================
# 2. Calculator
# ===============================
def calculator():
    a = float(input("Enter num1: "))
    b = float(input("Enter num2: "))
    op = input("Enter operation (+,-,*,/): ")

    if op == "+":
        print("Result =", a + b)
    elif op == "-":
        print("Result =", a - b)
    elif op == "*":
        print("Result =", a * b)
    elif op == "/":
        print("Result =", a / b)
    else:
        print("Invalid operation!")


# ===============================
# 3. Password Generator
# ===============================
def password_generator():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(chars)

    print("Generated Password:", password)


# ===============================
# 4. Rock Paper Scissors
# ===============================
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    user = input("Enter rock/paper/scissors: ")
    comp = random.choice(choices)

    print("Computer:", comp)

    if user == comp:
        print("Tie!")
    elif user == "rock" and comp == "scissors":
        print("You Win!")
    elif user == "paper" and comp == "rock":
        print("You Win!")
    elif user == "scissors" and comp == "paper":
        print("You Win!")
    else:
        print("Computer Wins!")


# ===============================
# 5. Word Counter
# ===============================
def word_counter():
    text = input("Enter sentence: ")
    words = text.split()
    print("Total words =", len(words))


# ===============================
# 6. To-Do List
# ===============================
def todo_list():
    tasks = []

    while True:
        print("\n1.Add Task  2.View Tasks  3.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            task = input("Enter task: ")
            tasks.append(task)
            print("Task Added!")

        elif ch == 2:
            print("Tasks:", tasks)

        elif ch == 3:
            break


# ===============================
# 7. Quiz App
# ===============================
def quiz_app():
    score = 0

    q1 = input("Capital of India? ")
    if q1.lower() == "delhi":
        score += 1

    q2 = input("5+5=? ")
    if q2 == "10":
        score += 1

    print("Final Score:", score, "/2")


# ===============================
# 8. Simple Chatbot
# ===============================
def chatbot():
    print("Chatbot started (type bye to stop)")

    while True:
        msg = input("You: ")

        if msg.lower() == "hi":
            print("Bot: Hello!")
        elif msg.lower() == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand")


# ===============================
# 9. Dice Roller
# ===============================
def dice_roller():
    print("Rolling Dice...")
    print("🎲 Number:", random.randint(1, 6))


# ===============================
# 10. BMI Calculator
# ===============================
def bmi_calculator():
    w = float(input("Enter weight (kg): "))
    h = float(input("Enter height (m): "))

    bmi = w / (h * h)
    print("BMI =", round(bmi, 2))


# ===============================
# 11. Multiplication Table
# ===============================
def table_print():
    n = int(input("Enter number: "))

    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


# ===============================
# 12. Countdown Timer
# ===============================
def countdown_timer():
    sec = int(input("Enter seconds: "))

    while sec > 0:
        print("Time left:", sec)
        time.sleep(1)
        sec -= 1

    print("⏰ Time Over!")


# ===============================
# 13. Age Calculator
# ===============================
def age_calculator():
    year = int(input("Enter birth year: "))
    current = datetime.now().year

    age = current - year
    print("Your Age =", age)


# ===============================
# 14. Simple Expense Tracker
# ===============================
def expense_tracker():
    amount = float(input("Enter expense amount: "))
    print("Expense Saved:", amount)


# ===============================
# 15. Random Joke Generator
# ===============================
def joke_generator():
    jokes = [
        "Why did the computer sleep? Because it had too many bugs 😄",
        "Why Python is easy? Because it's like English!",
        "Programmer's life: Eat, Code, Sleep!"
    ]

    print("😂 Joke:", random.choice(jokes))


# ===============================
# MAIN MENU
# ===============================
while True:
    print("\n==============================")
    print("   MINI PROJECTS (1 - 15)")
    print("==============================")
    print("1. Guessing Game")
    print("2. Calculator")
    print("3. Password Generator")
    print("4. Rock Paper Scissors")
    print("5. Word Counter")
    print("6. To-Do List")
    print("7. Quiz App")
    print("8. Chatbot")
    print("9. Dice Roller")
    print("10. BMI Calculator")
    print("11. Multiplication Table")
    print("12. Countdown Timer")
    print("13. Age Calculator")
    print("14. Expense Tracker")
    print("15. Joke Generator")
    print("16. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        guessing_game()
    elif choice == 2:
        calculator()
    elif choice == 3:
        password_generator()
    elif choice == 4:
        rock_paper_scissors()
    elif choice == 5:
        word_counter()
    elif choice == 6:
        todo_list()
    elif choice == 7:
        quiz_app()
    elif choice == 8:
        chatbot()
    elif choice == 9:
        dice_roller()
    elif choice == 10:
        bmi_calculator()
    elif choice == 11:
        table_print()
    elif choice == 12:
        countdown_timer()
    elif choice == 13:
        age_calculator()
    elif choice == 14:
        expense_tracker()
    elif choice == 15:
        joke_generator()
    elif choice == 16:
        print("Bye 👋 Program Closed")
        break
    else:
        print("Invalid choice!")
