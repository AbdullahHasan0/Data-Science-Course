import random

def current_state(live):
    stages = ['''
    +---+
    | |
    O |
    /|\ |
    / \ |
    |
    =========
    ''', '''
    +---+
    | |
    O |
    /|\ |
    / |
    |
    =========
    ''', '''
    +---+
    | |
    O |
    /|\ |
    |
    |
    =========
    ''', '''
    +---+
    | |
    O |
    /| |
    |
    |
    =========''', '''
    +---+
    | |
    O |
    | |
    |
    |
    =========
    ''', '''
    +---+
    | |
    O |
    |
    |
    |
    =========
    ''', '''
    +---+
    | |
    |
    |
    |
    |
    =========
    ''']
    print(stages[live])
    

def Hangman():
    print("Welcome To Hangman Game!! \n")
    word_list = ["aardvark", "baboon", "camel"]
    choosen_word = random.choice(word_list)
    display = []
    live = 6
    
    for letter in choosen_word:
        display += "_"
    while(True):
        if "_" not in display:
            print("\nCongratulations, You Won!!")
            break
        else:
            print(display)
            print("\n")
            guess = input("Guess A Letter :\n").lower()
            
            if guess in choosen_word:
                if guess not in display:
                    for i in range(len(choosen_word)):
                        if choosen_word[i] == guess:
                            display[i] = guess
                            
                else:
                    print("\nAlready Guessed That Letter!\n")
            else:
                if live == 0:
                    print('\nYou Lost!')
                    print("The Word Was",choosen_word)
                    break
                print("\nWrong Guess! Try Again.\n")
                live-=1
                print("Total Lives Remaining =",live)
                current_state(live)

if __name__ == "__main__":
    Hangman()