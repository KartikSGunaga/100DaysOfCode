text = input('What to print? ')
num = int(input('Enter the number of times to print: '))


def printNTimes(num, text):
    if(num == 0):
        return
    print(text)
    printNTimes(num-1, text)

printNTimes(num, text)