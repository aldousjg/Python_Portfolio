from random import choice

words_list = ["batman", "robin", "joker", "twoface", "riddler", "penguin", "bane", "catwoman"]
word = choice(words_list)
hint = "-" * len(word)
hint_list = list(hint)
lives = 8
guesses = []

print("Let's play HANGMAN! Guess the batman character!")

while lives > 0:
    print()
    print(hint)
    if "-" not in hint:
        print("You guessed the word!")
        print("You win!")
        break
    else:
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
        elif not guess.islower():
            print("Please enter a lowercase English letter")
        elif guess in guesses:
            print("You've already guessed this letter")
        elif guess in word:
            for i in range(0, len(word)):
                if guess == word[i]:
                    hint_list[i] = guess
                    hint = "".join(hint_list)
            guesses += guess
        else:
            print("That letter doesn't appear in the word")
            guesses += guess
            lives -= 1
            if lives > 0:
                print("You have {} lives left!".format(lives))
            elif lives == 0:
                print("You lose!")
                break
