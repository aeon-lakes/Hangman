# Hangman for Hyperskill 'Introduction to Python'
# I think I still see my 80's BASIC coding background coming through.

import random

word_pool = ['python', 'java', 'swift', 'javascript']

you_lost = 0

you_won = 0

play = True

def play_hangman():

    global you_lost

    global you_won

    solution = random.choice(word_pool)

    attempts = 8

    solution_list = list('-' * len(solution))

    guesses = []

    user_input = str()

    acceptable = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                  'x', 'y', 'z'}

    while attempts > 0:

        print(''.join(solution_list))
        print("Input a letter:")
        user_input = input()

        if len(user_input) != 1:
            print("Please, input a single letter.")

        elif user_input not in acceptable:
            print("Please, enter a lowercase letter from the English alphabet.")

        elif user_input in guesses:
            print("You've already guessed this letter.")

        elif user_input not in solution:
            print("That letter doesn't appear in the word")
            attempts -= 1

        if user_input not in guesses:
            guesses.append(user_input)

        for x in range(len(solution)):
            if solution[x] == user_input:
                solution_list[x] = user_input

                if '-' not in solution_list:
                    you_won += 1
                    print(f"You guessed the word {solution}!")
                    print("You survived!")
                    return

    you_lost += 1
    print("You lost!")
    return

print("H A N G M A N")

while play == True:
    print('Type "play" to play the game, "results" to show the scoreboard, '
          'and "exit" to quit:')
    user_selection = input()

    if user_selection == "exit":
        play = False
        exit()

    elif user_selection == "results":
        print(f"You won: {you_won} times")
        print(f"You lost: {you_lost} times")

    elif user_selection == "play":
        play_hangman()
