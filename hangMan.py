import random



word_list = ["camel", "baboon", "soccer"]


lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)

place_holder = ""

for position in range(len(chosen_word)):
    place_holder += "_"
print(place_holder)

game_over = False
correct_letters = []

while not game_over:# while game_over == false

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:

        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True

    if "_" not in display:
        game_over = True
        print("you win!")
