def printToN(num, i):
    if(i > num):
        return

    print(i)
    printToN(num, i+1)

num = int(input('enter the range: '))
start = int(input('From which number to start: '))
printToN(num, start)