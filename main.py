import random
import hangman_words
import hangman_art

print(hangman_art.logo)



chosen_word = random.choice(hangman_words.word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


display = ["_"]*word_length
Lives = 6
Game_over = False
while not  Game_over:

    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("YOU Already guessed this letter before")
        continue
    for index ,letter in enumerate(chosen_word):


        if letter == guess:
            display[index] = letter


        elif guess not in chosen_word:
            Lives -= 1
            print(f"{guess} is a wrong guess , you lose a life!")

            break

    print(f"Lives left: {Lives}")
    print(hangman_art.stages[Lives ])
    print("".join(display))
    if Lives == 0:
        print("Game Over ! You Lost !")
        print(f"{chosen_word} was the word :(")
        Game_over = True
    if "_" not in display:
        print("Game Over ! You won !")
        Game_over = True
