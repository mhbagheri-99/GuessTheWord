# Mohammad Hossein Bagheri
# 965361007
# put the text files in the same folder as the code and make sure the format .txt is visible not hidden
import random
import time
import os


def selectWord():       # chooses a random word
    categories = ["animals", "boy_names", "colors", "countries",
                  "fruits", "girl_names", "music_instruments"]
    n = random.randint(4, 7)
    randCat = random.sample(categories, n)
    myDict = {}
    for c in randCat:       # from each randomly chosen category picks 1 random word and put it in the dict
        file_path = os.path.dirname(__file__) + "\\" + c + ".txt"
        f = open(file_path, "r")
        values = []
        for w in f:
            values.append(w.replace("\n", ""))
        f.close()
        myDict.setdefault(c, values)
    selectedCat = random.sample(randCat, 1).pop()
    word = random.sample(myDict.get(selectedCat), 1).pop()      #chooses one random word from the dict
    alpha_filter = filter(str.isalpha, word)        #removes non alphabetic characters from the word (new zealand ---> newzealand)
    word = "".join(alpha_filter)
    return selectedCat + ":" + word     # returns word and category


def welcome():  # welcomes the user
    name = input("Enter your name: ")
    print("Welcome " + name + " :)")


def menu():  # shows the menu
    print("1.Guess the letters")
    print("2.Guess the word")
    print("3.Exit")
    print("# To get hint, enter * (you only have one hint and you MUST enter the hinted letter yourself)")
    while True:     # repaets the process until a valid option is selected
        selectedMode = input("Enter (1,2,3): ")
        if selectedMode == "1" or selectedMode == "2" or selectedMode == "3":
            break
        else:
            print("Enter a valid option")
    return selectedMode     # returns selected mode


def score_calc(t0,t1,time_limit,chances,hint):       # calculates score from the time it took to guess the word, number of chances left and if the hint is used
    t = t1 - t0
    if t > time_limit:
        score = chances * 10
    else:
        score = chances * (10+t)
    if hint:
        return score - 5
    else:
        return score


def guessTheWord(selectedMode):  # main function

    category, word = selectWord().split(":")
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    word = word.lower()
    word_list = list(word)
    word_letters = list(set(word_list))
    hint = False

    if selectedMode == "3":     # exits the program
        print("Have a good day :)")
        exit()

    else:
        n = float(input("Enter time limit in seconds: "))       # time limit set by the user
        print("The word category is a '" + category + "'!")
        enteredChars = []       # list of entered letters
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("_ " * len(word))
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        t0 = time.time()        # starts the timer
        if selectedMode == "1": # guess letter by letter
            chances = len(word) # number of chances
            while chances > 0:
                guessedLetter = input("Enter a letter: ").lower()   # lower case the word
                if guessedLetter.isalpha():     # checks the input to be an alphabet
                    if guessedLetter in enteredChars:   # checks if it was entered before
                        print("You've entered " + guessedLetter + " before!")
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    elif len(guessedLetter) > 1:        # checks if 1 letter is entered
                        print("Enter ONE letter each time!")
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    else:
                        enteredChars.append(guessedLetter)  # add the letter to the entered letters list
                        if guessedLetter in word:
                            print("Goodjob, Keep on guessing!")
                            for i in range(len(word)):      # updates the blanks
                                if guessedLetter == word[i]:
                                    new_blanks_list[i] = word_list[i]
                        
                        if new_blanks_list == blanks_list:
                            print("Your letter isn't here.")
                            chances = chances - 1   # lower the chances by 1
                            if chances > 0:     # if any chances left
                                print("Guess again. Chances left: " + str(chances))
                                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                print(' '.join(blanks_list))
                                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

                            else:       # loses the game if word's not guessed and chances = 0
                                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                print("You lost :(")
                                print("The word was " + word + ".")
                                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                while True:     # restarts the game if user wants
                                    m = input("You wanna play again? (yes/no): ")
                                    if m == "yes":
                                        start()
                                    elif m == "no":
                                        print("Have a good day :)")
                                        exit()
                                    else:
                                        print("Enter a valid option")
                                

                        elif word_list != blanks_list:  # if letter is in the word
                            blanks_list = new_blanks_list[:]
                            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                            print(' '.join(blanks_list))    # updates the blanks
                            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                            if word_list == blanks_list:    # if the word is guessed and completed
                                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                print("\nYOU WIN! ƪ(˘⌣˘)ʃ Here is your prize:")
                                t1 = time.time()        # stops the timer
                                print(score_calc(t0,t1,n,chances,hint)) # prints the score using score func
                                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                while True:     # restarts the game if user wants
                                    m = input("You wanna play again? (yes/no): ")
                                    if m == "yes":
                                        start()
                                    elif m == "no":
                                        print("Have a good day :)")
                                        exit()
                                    else:
                                        print("Enter a valid option")
                                

                else:       # if entered char is not alphabet
                    if guessedLetter == "*" and hint == False:  # gives the hint letter randomly
                        hint = True
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        print("*** Enter " + random.choice(list(set(word_letters) - set(enteredChars))) + " ***")
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    else:   # prints error
                        print("Enter an alphabet!")
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


        if selectedMode == "2": #guess the whole word (almost like above)
            chances = 1
            while True:
                guessedWord = input("Enter your guessed word: ").lower()
                t0 = time.time()
                if guessedWord == "*" and hint == False:
                    hint = True
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("*** The word has " + random.choice(word_letters) + " ***")
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                elif guessedWord != word:
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("You lost :(")
                    print("The word was " + word + ".")
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    while True:
                        m = input("You wanna play again? (yes/no): ")
                        if m == "yes":
                            start()
                        elif m == "no":
                            print("Have a good day :)")
                            exit()
                        else:
                            print("Enter a valid option")
                                
                elif guessedWord == word:
                    t1 = time.time()
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("\nYOU WIN! ƪ(˘⌣˘)ʃ Here is your prize:")
                    print(score_calc(t0,t1,n,chances,hint))
                    while True:
                        m = input("You wanna play again? (yes/no): ")
                        if m == "yes":
                            start()
                        elif m == "no":
                            print("Have a good day :)")
                            exit()
                        else:
                            print("Enter a valid option")


def start():  # initializes the game
    welcome()
    guessTheWord(menu())


start()
