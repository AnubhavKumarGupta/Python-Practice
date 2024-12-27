import random

def get_word():
    words = ['python', 'programming', 'computer', 'algorithm', 'data', 'science']
    return random.choice(words)

def play():
    word = get_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Print used letters and remaining lives
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # Print current word with underscores for missing letters
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # Get user input (a letter)
        user_letter = input('Guess a letter: ').lower()

        if user_letter in alphabet - used_letters:
            # Add letter to used letters set
            used_letters.add(user_letter)
            if user_letter in word_letters:
                # Remove letter from word letters set if it is in the word
                word_letters.remove(user_letter)
            else:
                # Decrement lives if letter is not in word
                lives -= 1
                print('Letter is not in word.')
        elif user_letter in used_letters:
            # Warn user if letter has already been used
            print('You have already used that letter. Please try again.')
        else:
            # Warn user if input is invalid
            print('Invalid input. Please try again.')

    # Game is over
    if lives == 0:
        print('You died. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, 'in', 6-lives, 'tries.')
