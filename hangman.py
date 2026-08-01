import random

words = ["apple", "tiger", "house", "chair", "plant"]

word = random.choice(words)
guessed = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")

    elif guess in word:
        guessed.append(guess)
        print("Correct!")

    else:
        guessed.append(guess)
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Game Over! The word was:", word)