name = input('Enter your name: ')

list_name = [letter.upper() for letter in name]
print(list_name)

range_list = [num*2 for num in range(1, 5)]
print(range_list)