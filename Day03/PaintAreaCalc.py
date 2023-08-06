#Write your code below this line 👇
import math






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works. 
def paint_calc(height, width, cover):
    cans = (height * width) / cover
    # print(cans)
    cans = math.ceil(cans)
    print(f"You'll need {cans} cans of paint.")  

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)