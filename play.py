import random
import os

def run():


    IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
 =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
 =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
 =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
 =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
 =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
 =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
 =========''']


    DB = [
        "C",
        "PYTHON",
        "CARACAS",
        "VENEZUELA",
        "KARLAS",
        "ALEJANDRO",
        "RICARDO"
    ]


    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])
        letter = input("Elige una letra ").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
        
        if not found:
            attemps -= 1 
        
        if "_" not in spaces:
            os.system("clear")
            print("Bien Hecho Ganaste!!")
            break
            input()
        
        if attemps == 0:
            os.system("clear")
            print("Lo siento sigue intentando perdiste")
            break
            input()





if __name__ == "__main__":
    run()

