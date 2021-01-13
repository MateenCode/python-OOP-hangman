import random

class Word():
    def __init__(self, chosen_word):
        self.chosenWord = chosen_word
        self.guessedWord = ""
        self.correctGuessedLetters = []
        self.wrongGuessedLetters = []

        for i in range(len(self.chosenWord)):
            if (i != len(self.chosenWord) - 1):
                self.guessedWord += "_ "
            else: 
                self.guessedWord += "_"


    def getGuessedWord(self):
        return self.guessedWord

    def getWrongGuessedLetters(self):
        return self.wrongGuessedLetters

    def setGuessedWord(self, string): 
        self.guessedWord = string
        

    def guessAllLetters(self, char):
        toReturn = ""
        if (char.isalpha()):
            char = char.lower()
            for index in range(0, len(self.chosenWord)):
                if (self.chosenWord[index].lower() == char):
                    toReturn += char
                    self.correctGuessedLetters.append(char)
                else: 
                    if self.chosenWord[index].lower() in self.correctGuessedLetters:
                        toReturn += self.chosenWord[index]
                    elif (index != len(self.chosenWord) - 1):
                        toReturn += "_ "
                    else: 
                        toReturn += "_"
            if (toReturn == self.getGuessedWord()):
                self.wrongGuessedLetters.append(char)
            self.setGuessedWord(toReturn)
            # print(self.correctGuessedLetters)
            # print(self.wrongGuessedLetters)
                    
    def isWordGuessed(self):
        for letter in self.guessedWord:
            if (letter == "_"):
                return False
        return True
    
    def __str__(self):
        return self.guessedWord

if __name__ == '__main__':
    isPlaying = True
    listOfWords = ["acres",
                    "batch",
                    "bulk",
                    "bunch",
                    "bundle",
                    "cargo",
                    "clump",
                    "collection"]
    # currentWord = Word(random.choice(listOfWords))
    currentWord = Word("acres")

    while (isPlaying):
        currentGuess = currentWord.getGuessedWord()
        print("Current Word: " + currentGuess)
        print("Wrong guesses wrong: " + str(currentWord.getWrongGuessedLetters()))
        # print(currentWord.getWrongGuessedLetters)
        userGuess = input("Guess a letter in the word above!")
        if (len(userGuess) == 1): 
            currentWord.guessAllLetters(str(userGuess))
            newGuess = currentWord.getGuessedWord()
            
            if (currentGuess != newGuess):
                print("Correct Guess")
            else:
                print("Wrong Guess")


            if(currentWord.isWordGuessed()):
                isPlaying = False
                print("You win! The word is: "+  str(currentWord))
        else: 
            print("please put in a ONLY a letter")



