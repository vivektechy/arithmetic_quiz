import random
from traceback import format_exc

print("Welcome to the Arithmetic Puzzle Game!")
print("Choose a difficulty level:")
print("1. Easy\n2. Medium\n3. Hard")

try:
    level = int(input("Enter your choice (1/2/3): "))
    if level not in [1,2,3]:
        print("Invalid Choice. Please selct valid level : ")
    else:
        score=0
        for i in range (5):
            if level==1:
                num1, num2 = random.randint(1, 10), random.randint(1, 10)
                operator = random.choice(['+', '-'])
            elif level == 2:
                num1, num2 = random.randint(1, 20), random.randint(1, 20)
                operator = random.choice(['+', '-', '*'])
            else:
                num1, num2 = random.randint(10, 50), random.randint(10, 50)
                operator = random.choice(['+', '-', '*'])
            question=f"{num1} {operator} {num2}"
            answer=eval(question)
            print(f"Solve: {question}")
            try:
                user_answer = int(input("Your answer: "))
                if user_answer == answer:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {answer}\n")
            except ValueError:
                print(f"Invalid input. The correct answer was {answer}\n")

        print(f"Game Over! Your score: {score}/5")
except ValueError:
    print("Invalid choice. Please enter a valid number.")
