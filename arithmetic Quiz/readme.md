'''
                                                                                                              # Arithmetic Puzzle Game in Python

This is a Python console-based arithmetic puzzle game that challenges users with random math problems across three difficulty levels. The game tracks the user's score and provides feedback on their answers.

## Features
- Three difficulty levels:
  - **Easy:** Numbers between 1-10 with addition (+) and subtraction (-).
  - **Medium:** Numbers between 1-20 with addition (+), subtraction (-), and multiplication (*).
  - **Hard:** Numbers between 10-50 with addition (+), subtraction (-), and multiplication (*).
- Five random questions per session.
- Provides immediate feedback for correct or incorrect answers.
- Tracks and displays the user's final score out of 5.
- Handles invalid inputs gracefully.

## How to Run the Code
1. Install Python (if not already installed) from [python.org](https://www.python.org/downloads/).
2. Copy the code into a Python file, e.g., `arithmetic_puzzle.py`.
3. Run the file using the command:
   ```bash
   python arithmetic_puzzle.py
   ```
4. Follow the instructions displayed on the screen.

## Code Explanation

### 1. Importing Libraries
```python
import random
```
- The `random` library is used to generate random numbers and operators for the quiz.

### 2. Displaying Menu and Taking Input
```python
print("Welcome to the Arithmetic Puzzle Game!")
print("Choose a difficulty level:")
print("1. Easy\n2. Medium\n3. Hard")
```
- The program displays a welcome message and asks the user to choose a difficulty level.

### 3. Difficulty Selection and Validation
```python
try:
    level = int(input("Enter your choice (1/2/3): "))
    if level not in [1, 2, 3]:
        print("Invalid choice. Please select a valid level.")
```
- The user enters their desired difficulty level.
- If an invalid choice is entered, an error message appears.

### 4. Generating Random Questions
```python
if level == 1:
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    operator = random.choice(['+', '-'])
elif level == 2:
    num1, num2 = random.randint(1, 20), random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
else:
    num1, num2 = random.randint(10, 50), random.randint(10, 50)
    operator = random.choice(['+', '-', '*'])
```
- Numbers are generated based on the selected difficulty level.
- The `random.choice()` function picks an arithmetic operator randomly.

### 5. Evaluating the Answer
```python
question = f"{num1} {operator} {num2}"
answer = eval(question)
```
- The `eval()` function computes the correct answer by evaluating the expression as a string.

### 6. Checking User's Answer
```python
user_answer = int(input("Your answer: "))
if user_answer == answer:
    print("Correct!\n")
    score += 1
else:
    print(f"Wrong! The correct answer was {answer}\n")
```
- The program compares the user's answer with the calculated answer and updates the score accordingly.

### 7. Displaying Final Score
```python
print(f"Game Over! Your score: {score}/5")
```
- After all 5 questions, the user's total score is displayed.

## Future Enhancements
To improve the game further, you could add:
- A timer for each question.
- More challenging arithmetic operations like division or power.
- A scoring leaderboard.
- Multiple rounds for extended gameplay.

## License
This project is open-source and free to use for educational and learning purposes.
'''


