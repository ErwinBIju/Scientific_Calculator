import math

def add(*args):
    return sum(args)

def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    result = args[0]
    try:
        for num in args[1:]:
            result /= num
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    return result

def exponent(*args):
    result = args[0]
    for num in args[1:]:
        result **= num
    if result > 100000000:
        result = "Value too Large"
    else:
        return result

def squareRoot(x):
    if x <= 0:
        raise ValueError("Cannot take the square root of a negative number.")
    else:
        return math.sqrt(x)
    
def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def main():
    while True:
        result = calculations()
        while True:
            try_again = input("Do you want to use the result for another calculation? (Y/N): ").lower()
            if try_again == 'y':
                result = calculations(previous_result=result)
            elif try_again == 'n':
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        
        
        new_calc = input("Do you want to start a new calculation? (Y to start new, anything else to exit): ").strip().lower()
        if new_calc != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break

            

    
   
    
def calculations(previous_result = None):
    print("Welcome to the multi-number calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")
    if choice in ['1', '2', '3', '4', '5']:
        
        if previous_result is not None:
            numbers = input("Enter numbers separated by spaces: ")
            num_list = [previous_result] + [float(num) for num in numbers.split()]
            
            operations = {
                '1': add,
                '2': subtract,
                '3': multiply,
                '4': divide,
                '5': exponent
            }
            operation_func = operations[choice]
        
            result = operation_func(*num_list)
            print(f"The result is: {result}")
            
        else:
            numbers = input("Enter numbers separated by spaces: ")
            num_list = [float(num) for num in numbers.split()]
            
            operations = {
                '1': add,
                '2': subtract,
                '3': multiply,
                '4': divide,
                '5': exponent
            }
            operation_func = operations[choice]
        
            result = operation_func(*num_list)
            print(f"The result is: {result}")
            


    elif choice in ['6', '7', '8', '9']:
        if previous_result is not None:
            
            operations2 = {
                '6': squareRoot,
                '7': sine,
                '8': cosine,
                '9': tangent
            }
            operation2_func = operations2[choice]
            result = operation2_func(previous_result)
            print(f"The result is: {result}")
            
        else:
            number = float(input("Enter the number: "))
            operations2 = {
                '6': squareRoot,
                '7': sine,
                '8': cosine,
                '9': tangent
            }
            operation2_func = operations2[choice]
            result = operation2_func(number)
            print(f"The result is: {result}")
    else:
        print("invalid choice")
        
    return result
main()