# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = (name1 + name2).upper()

countT = 0
countR = 0
countU = 0
countE = 0
count1 = 0

countl = 0
counto = 0
countv = 0
counte = 0
count2 = 0

countT = name.count("T")
countR = name.count("R")
countU = name.count("U")
countE = name.count("E")
count1 = countT + countR + countU + countE

countl = name.count("L")
counto = name.count("O")
countv = name.count("V")
counte = name.count("E")
count2 = countl + counto + countv + counte

count = count2 + count1*10

if(count < 10 or count > 90):
    print(f"Your score is {count}, you go together like coke and mentos.")
elif(count < 50 and count > 40):
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")