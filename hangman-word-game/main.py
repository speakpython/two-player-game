#https://speakpython.codes/two-player-game/2023/03/07/hangman-word-game.html#puzzle-hint-and-answer

from getpass import getpass
import math, random

string = getpass("\nProvide Puzzle Answer (Player 1) : ").strip().replace(" ", "").casefold()
hint = input('Any Hint : ')


#https://speakpython.codes/two-player-game/2023/03/07/hangman-word-game.html#random-puzzle-design

def auto_puzzle(puzzle, missing_words = ""):
    for i in range((len(puzzle)//2)):
        random_value = puzzle[math.floor(random.random()*len(puzzle))]
        if random_value not in missing_words:
            missing_words += random_value
    for a in range(len(puzzle)):
        if puzzle[a] in missing_words:
            puzzle = puzzle.replace(puzzle[a],'_')
    return puzzle, missing_words


#https://speakpython.codes/two-player-game/2023/03/07/hangman-word-game.html#custom-puzzle-design

def custom_puzzle(puzzle, missing_words = ""):
    num_blanks = int(input('How many blanks you prefer? : '))
    while len(missing_words) < num_blanks:
        blank_char = input('which character you want to blanked : ')
        if blank_char in puzzle:
            puzzle = puzzle.replace(blank_char,'_')
            missing_words += blank_char
            print(puzzle)
        else:
            print('Element not exist in Puzzle')
    return puzzle, missing_words


#https://speakpython.codes/two-player-game/2023/03/07/hangman-word-game.html#validating-guesses

def check_for_guess(puzzle, string, missing_words):
    false_attempt = 0
    while false_attempt < len(missing_words):
        if puzzle == string.lower():
                break
        ask = 'Remain Attempt : {} | Guess a Word (unique) : '.format(len(missing_words)-(false_attempt))
        guess = input(ask).casefold()
        if guess in missing_words and len(guess) == 1:
            for a in range(len(puzzle)):
                if string[a].lower() == guess:
                    puzzle = puzzle[:a] + guess + puzzle[a+1:]
            print('Keep it on ',puzzle)
        else:
            false_attempt += 1
            print('Oops! Try again')
    return puzzle


#https://speakpython.codes/two-player-game/2023/03/07/hangman-word-game.html#understanding-the-driver-code

puzzle = string
if len(string) < 6:
    print('Answer should be > 6 characters')
else:
    false_attempt = 0
    puzzle_type = input('\nDo you want system designed puzzle? y/n : ')
    puzzle, missing_words = auto_puzzle(puzzle) if puzzle_type == 'y' or puzzle_type == 'Y' else custom_puzzle(puzzle)
    print('\n\nYour Puzzle (Player 2):',puzzle)
    print('Given hint: ',hint)
    given_answer = check_for_guess(puzzle, string, missing_words)
    print('\nCongratulation you won, Player 1 lost!') if given_answer == string.lower() else print('\nYou lost, Player 1 Won')
