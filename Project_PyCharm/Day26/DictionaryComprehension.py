sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words = sentence.split()
print(words)

len_list = [len(word) for word in words]
print(len_list)
dict_tup = []

for i in range(len(words)):
    pair = (words[i], len_list[i])
    dict_tup.append(pair)

print(dict_tup)
result = dict(dict_tup)

print(result)