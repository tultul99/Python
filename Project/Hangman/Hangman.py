
import string
from words import words
import random

def get_words() :
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman() :
    word = get_words()
    word_letters = set(word)      # {'A', 'S', 'T', 'N'}
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    live = 6

    while len(word_letters) > 0 and live > 0:
        print(f"You've tried these letters: {' '.join(used_letters)}")
        
        word_list = [letter if letter in used_letters else '_' for letter in word]

        print(f"Current word is: {' '.join(word_list)}")
    
        user_letter = input ('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                live -= 1
        
        elif user_letter in used_letters:
            print("You've already used it once.")
        
        else:
            print("You've input an invalid character.")
    
    print(f"Congrats!!! You guessed the word {word}")

hangman()
