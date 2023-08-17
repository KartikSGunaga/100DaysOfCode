import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

letter_list = []
code_list = []

for (index, row) in data.iterrows():
    letter_list.append(row.letter)
    code_list.append(row.code)

i = -1
code_dictionary = []
for letter in letter_list:
    i += 1
    pair = (letter, code_list[i])
    code_dictionary.append(pair)

codes = dict(code_dictionary)
print(codes)

name = input('enter the name: ')
name_list = [letter.upper() for letter in name]
print(name_list)

code_name = []

for i in range(len(name_list)):
    for key in codes:
        if(name_list[i] == key):
            code_name.append(codes[key])

print(code_name)
