def factorial(num):
    if(num == 0 or num == 1):
        return 1

    return (num * factorial(num - 1))

num = int(input('Enter the number: '))

print(f"The factorial of {num} is {factorial(num)}.")