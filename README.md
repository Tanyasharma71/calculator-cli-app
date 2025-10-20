Calculator CLI App

A simple and interactive Command-Line Calculator built in Python. This tool allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division directly in the terminal.

📘 Features

Perform Addition, Subtraction, Multiplication, and Division

Handles division by zero errors gracefully

Interactive menu-based interface

User-friendly error messages for invalid inputs

Loops until the user chooses to exit

🚀 How to Run

Clone or download the repository:

https://github.com/Tanyasharma71/calculator-cli-app.git

Run the script:

python calculator.py

🧮 Usage Guide

When you run the app, a menu will appear like this:

========================================
      CALCULATOR CLI APP
========================================
Select an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
========================================

Then, follow these steps:

Choose an operation (1–5)

Enter two numbers when prompted

View your result instantly

Example Run

Welcome to Calculator CLI App!

========================================
      CALCULATOR CLI APP
========================================
Select an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
========================================

Enter your choice (1-5): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0

Do you want to perform another calculation? (y/n): n

Thank you for using Calculator CLI App!
Goodbye! 👋

⚠️ Error Handling

If you enter non-numeric input → displays Error: Please enter valid numbers

If you divide by zero → displays Error: Division by zero is not allowed

If you select an invalid menu option → displays Error: Invalid choice! Please select 1-5

📄 Code Overview

Main Functions:

add(a, b): Returns the sum of two numbers

subtract(a, b): Returns the difference

multiply(a, b): Returns the product

divide(a, b): Handles division safely with error check

display_menu(): Prints the calculator options

get_numbers(): Gets user input safely

calculator(): Controls the overall program flow

 Future Enhancements

Add exponentiation and square root operations

Allow multiple operations in one expression

Include history of calculations

Add colorized CLI output

