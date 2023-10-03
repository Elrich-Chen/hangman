import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(" ")
word = random.choice(someWords)

print('''RULES OF THE GAME:
1. YOU CAN ONLY ENTER A SINGLE CHARACTER AT A TIME
2. ENTERING A CORRECT LETTER WILL BE REVEALED TO YOU
3. A WRONG INPUT WILL COST YOU ONE CHANCE \n''')
print("GUESS THE Name of the Word ! Hint: its the name of a fruit <3")

for i in word:
    print("_", end=" ")
print()

playing = True
letterGuessed = ''
chances = len(word)+2

while playing:
    print()
    chances -= 1
    print(f"You have {chances} chances left !")

    guess = (str(input("Enter a letter to guess : "))).lower()

    if not guess.isalpha():
        print("Enter Only A Letter !")

    elif len(guess) > 1:
        print("Enter Only a Single Letter !")

    elif guess in letterGuessed:
        print("You Have Already Guessed That Letter !")
    
    else:
        if guess in word:
            k = word.count(guess)
            for _ in range(k):
                letterGuessed = letterGuessed + guess

        if Counter(letterGuessed)!= Counter(word):
            for char in word:
                if char in letterGuessed:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
        else:
            print()
            print(f"The word was {word}!")
            print("Congrats, You have won ! ")
            playing = False

    if chances <= 1:
        playing = False
        print("")
        print("Sorry the game is over, You have Lost :( Better luck next time ! ")
        print(f"the word was {word}!")
    














            
