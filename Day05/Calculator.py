# Get the first number from the user as input
num1 = float(input('What\'s the first number?' ))

# Function to perform calculation
def calc(num1):
    # Display the available operations
    print(" +  -  /  *  ")
    
    # Get the desired operation from the user
    operation = input('Pick an operation from the above list: ')
    
    # Get the second number from the user
    num2 = float(input('What\'s the second number? '))
    
    # Initialize the answer variable
    answer = 0.0

    # Perform the selected operation
    if(operation == "+"):
        addition(num1, num2)
    elif(operation == "-"):
        subtraction(num1, num2)
    elif(operation == "*"):
        multiplication(num1, num2)
    elif(operation == "/"):
        division(num1, num2)
    else:
        print("Invalid choice")
        return 0

# Function to perform addition
def addition(num1, num2):
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")
    proceed(answer)

# Function to perform subtraction
def subtraction(num1, num2):
    answer = num1 - num2
    print(f"{num1} - {num2} = {answer}")
    proceed(answer)

# Function to perform multiplication
def multiplication(num1, num2):
    answer = num1 * num2
    print(f"{num1} * {num2} = {answer}")
    proceed(answer)

# Function to perform division
def division(num1, num2):
    answer = num1 / num2
    print(f"{num1} / {num2} = {answer}")
    proceed(answer)

# Function to proceed with another calculation or exit
def proceed(answer):
    boolean = input('Do you wish to proceed? y or n? ')
    if(boolean == 'y'):
        calc(answer)
    else:
        answer = 0
        print('Thank you!')
        return 0

# Start the calculation process with the initial number
calc(num1)
