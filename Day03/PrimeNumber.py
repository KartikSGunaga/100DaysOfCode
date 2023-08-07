num = int(input('Enter the number: '))

# count = 0

def isPrime(num):
    count = 0
    for i in range(2, num):
        if(num % i == 0):
            count += 1
            break
    
    if(count != 0):
        return("It's not a prime number.")
    else:
        return("It's a prime number.")

print(isPrime(num))