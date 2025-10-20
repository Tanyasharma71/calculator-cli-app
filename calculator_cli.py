"""
Calculator CLI App
A command-line calculator supporting basic arithmetic operations
Author: Python Developer Intern
"""

def add(a, b):
    """Addition operation"""
    return a + b

def subtract(a, b):
    """Subtraction operation"""
    return a - b

def multiply(a, b):
    """Multiplication operation"""
    return a * b

def divide(a, b):
    """Division operation"""
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("      CALCULATOR CLI APP")
    print("="*40)
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)

def get_numbers():
    """Get two numbers from user input"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers")
        return None, None

def calculator():
    """Main calculator function"""
    print("\nWelcome to Calculator CLI App!")
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("\nThank you for using Calculator CLI App!")
            print("Goodbye! 👋")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            
            if num1 is None or num2 is None:
                continue
            
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
            # Ask if user wants to continue
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ")
            if continue_calc.lower() != 'y':
                print("\nThank you for using Calculator CLI App!")
                print("Goodbye! 👋")
                break
        else:
            print("\nError: Invalid choice! Please select 1-5")

if __name__ == "__main__":
    calculator()
