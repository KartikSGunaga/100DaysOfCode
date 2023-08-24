def sumOf(num):
    if(num == 0):
        return 0

    return num + sumOf(num -1)

num = int(input('enter the range: '))
print(f"Sum of numbers from 1 to {num} is: {sumOf(num)}")