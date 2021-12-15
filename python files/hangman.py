import random
import string


class Hangman(object):
    words = ['moon', 'sun', 'earth', 'sky'] 
    
    def main(self):
        word = random.choice(self.words).upper()
        word_letters = set(word)
        alphabet = set(string.ascii_uppercase)
        used_letters = set()
        lives = 6
        print('Welcome to Hangman!')
        
        while len(word_letters) > 0 and lives > 0:
            
            print(f'You have {lives} lives left and you have used these letters',' '.join(used_letters))
            
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('Current word: ',' '.join(word_list))
            
            user_letter = input('Guess a letter:').upper()
            print()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                 
                else:
                    lives -= 1
                    print('Letter is not in word')
                    
            elif user_letter in used_letters:
                print('You have already used that character. Please try again')
                
            else:
                print('Invalid character. Please try again')
        if lives == 0:
            print('You died, Sorry. The word was',word)
        print('You guessed the word', word, '!!!')
        
user = Hangman()
user.main()
    