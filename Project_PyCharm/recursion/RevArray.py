def revArr(arr, i, rev):
    n = len(arr)
    if i >= n / 2:
        return

    temp = arr[i]
    arr[i] = arr[n - i - 1]
    arr[n - i - 1] = temp

    revArr(arr, i + 1, rev)

length = int(input('Enter the length: '))
arr = [1, 2, 3, 4, 5, 6]

print("Original array:", arr)
revArr(arr, 0, [])

print("Reversed array:", arr)


