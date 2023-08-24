def printToN(num):
    if(num == 0):
        return

    print(num)
    printToN(num-1)

num = int(input('Enter the range: '))
printToN(num)