# Import the random module here
import random
# Split string method
names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
#names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num = random.randint(0, len(names_string)-1)
#print(len(names_string), num)

print(names_string[num] + " is going to buy the meal today!")
