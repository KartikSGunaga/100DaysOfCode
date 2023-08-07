import random

words = ["dog", "cat", "horse", "cow", "pig", "sheep", "chicken", "duck", "goose", "fish",
         "apple", "banana", "orange", "grape", "watermelon", "strawberry", "pear", "peach", "plum", "pineapple",
         "carrot", "potato", "onion", "tomato", "lettuce", "cucumber", "broccoli", "spinach", "celery", "zucchini",
         "car", "house", "tree", "book", "chair", "table", "phone", "computer", "TV", "lamp",
         "city", "country", "park", "beach", "mountain", "river", "lake", "ocean", "forest", "desert",
         "man", "woman", "child", "boy", "girl", "teacher", "doctor", "nurse", "police officer", "firefighter",
         "run", "jump", "eat", "sleep", "swim", "dance", "sing", "play", "read", "write"]

random_word = random.choice(words).lower()
word = list(random_word)
print(word)
length = len(word)
chances = 6
guess_word =[]

for step in range(length):
    guess_word.append("_")

strWord = "".join(guess_word)
print(strWord)

for i in range(chances):
    if(guess_word == word):
        # print("".join(guess_word), end = "")
        # print(": You've guessed it!")
        break
    #strWord = "".join(guess_word)
    else:
        print(f"You have {chances - i} chances.")
        print(guess_word)  
        guess = input("Guess the letter: ").lower()
        if(guess in word):
            print("right guess!")
            for letter in range(length):
                if(word[letter] == guess):
                    guess_word[letter] = guess
                else:
                    continue
        else:
            print("Wrong guess")
            continue
        
if(guess_word == word):
    print("".join(guess_word), end = "")
    print(": You've guessed it!")
    #strWord = "".join(guess_word)
else:
    print("The word was ",  end="")
    print("".join(guess_word), end = "")