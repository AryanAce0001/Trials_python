import random
import string
from words import words

def get_valid_words(words):
    word=random.choice(words)   # randomly chooses something from the list
    while '-' or ' ' in word:
        word= random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)    # letters in the word
    alphabet= set(string.ascii_uppercase)
    used_letter= set()  # letters user has guessed

    #getting user input
    while len(word_letters) > 0:
        
        # letters used 
        print('You\'ve already used these letters ', ' '.join(used_letter ))

        # what the current word is (like this ramble will be R_M__E)
        word_list = [letter if letter in used_letter else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter=input('Guess the letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letter:
            print('You have already used that character! Please try another letter')

        else:
            print('Invalid character. Please try again.')
    
hangman()