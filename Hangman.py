import random
def ChooseRandomWord():
    #This function picks a random word from the SOWPODS dictionary
    words = []
    with open('SowpodsDictionary.txt') as f:
        line = f.readline()
        while line:
            words.append(line)
            line = f.readline()
    word = words[random.randint(1, len(words))]
    return word

def NextLetter():
    #This function takes user guess
    letter = input("Guess your letter: ")
    return letter.upper()

def GenerateWordString(word,LettersGuessed):

    output =[]
    for letter in word:
        if letter in LettersGuessed:
            output.append(letter.upper())
        else:
            output.append("_")
    return ''.join(output)

def PrintHangman(Guesses):
    if (6 - Guesses) == 6:
        print("-----|")
    elif (6 - Guesses) == 5:
        print("-----|\n     O")
    elif (6 - Guesses) == 4:
        print("-----|\n     O\n    ( )")
    elif (6 - Guesses) == 3:
        print("-----|\n     O\n   /( )")
    elif (6 - Guesses) == 2:
        print("-----|\n     O\n   /( )/")
    elif (6 - Guesses) == 1:
        print("-----|\n     O\n   /( )/\n    /")
    elif (6 - Guesses) == 0:
        print("-----|\n     O\n   /( )/\n    //")

if __name__ == '__main__':
    word = ChooseRandomWord()

    LettersToGuess = set(word)
    CorrectLetters = set()
    IncorrectLetters = set()
    Guesses = 0

    print("Welcome to Hangman!")
    WordString = GenerateWordString(word, CorrectLetters)
    print("WORD: " + WordString)

    while(len(LettersToGuess) > 0) and Guesses < 6:

        guess = NextLetter()

        if guess in CorrectLetters or guess in IncorrectLetters:
            print("You already guessed that letter.")
            continue

        if guess in LettersToGuess:
            LettersToGuess.remove(guess)
            CorrectLetters.add(guess)
        else:
            IncorrectLetters.add(guess)
            Guesses += 1

        print("WORD: " + WordString)
        print("You have {} guesses left".format(6 - Guesses))
        PrintHangman(Guesses)

    if Guesses < 6:
        print("Congratulations! You correctly guessed the word {}".format(word))
    else:
        print("Sorry, you lost! The correct word was {}".format(word))




















































