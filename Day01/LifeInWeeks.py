# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_age = 90 - int(age)

days = int_age * 365
weeks = int_age * 52
months = int_age * 12 

print('You have ' + str(days) + " days, " + str(weeks) +" weeks, and " + str(months) + " months left.")