# Author: Aman Ayaz
# Date: 2018/05/23
# About: HangMan

start = ""
while start != "NO": # Forever repeat the code, corresponds to teh last statement aswell. 
    import random # This imports the randint function so I can randomize which word will be chosen.

    def image():
        print ("+---+")
        print ("    |   ")
        print ("    |   ")  
        print ("    |   ")
        print ("    === ")
        return ("")
    
    def Enter(): # This method helps witht the welcome intro. Asks for the person's name, and starts 
                 # the code continuing to the next part of the code. 
        name = input ("Enter your name.")
        print ("Welcome", name, "to the Hangman Game")
        print ("Try to guess the word in 6 tries or less")
        image()
        print ()
    Enter()
    def previous(previous,guess): # Method that checks if the previous guess is not in the guess. 
        return guess not in previous
        
    def letterInvestigator(guess, word, blankword,chances): #Checks if the guessed letter exists within the word. If yes, it replaces 
                                                            #the blank phrase with the letters in the same place that they exist in the phrase. 
    
        difference = 1 # This difference variable defines the chances. If the guess is not in the word, 
                       # the difference is set to 1. If it is, the difference is set to 0. 
                       # This difference is then sent to the chance method which will either result in the chance variable 
                       # decreasing (if difference is 1) or staying the same (if difference is 0).
    
        if guess in word: # if guess is in the word
            for i in range(0, len(word)): # checking each placement or each character or "_" to repleace. 
                if (word[i] == guess): # If the guess is correct.
                    blankword[i] = guess # If blank word is the same as guess. 
                    difference = 0 # no life is being deducted.
        
        return difference
    
    def answer(): #This method turns the list into a string.
        newword = ""
        for i in word:
            newword = newword + i  
        return newword

    def fail(failed): #Keeps track of which letters have been guessed and which are incorrect. 
                      #It can be displayed so that the person doesn't make the same mistake again.
        if guess not in word:
            failed = failed + guess
        return failed   
    
    def chance(chances,difference):#Checks the # of the person's chances. 
        chances = chances - difference
        return chances
    
    failed = "" #Defines the failed variable to blank, which will later be filled.
    previouss = "" # Defines the previous variable which decides the to 
    chances = 6 #Defines the number of lives the person has before they lose 
    wordlist = [ ["c","a","n"] , ["l","e","f","t"], ["c","o","m","p","u","t","e","r"] , ["w","a","t","e","r"] , ["b","o","l","t","s"] , ["v","i","s","i","o","n"]] #This is the phrase list, consisting of 6 different words; can, science, computer, water, bolts, vision.
    num = random.randint(0,len(wordlist)-1) #Generates a random num, automatically will choose which word the person has to guess.
    word = (wordlist[num]) 
    newword = answer()
    blankword = ["_"]*len(word) #Defines the blank phrase which the user needs to fill in
    

    while chances > 0: #Allows the person to guess as long as they still have chances left.                 
        print("You have", chances, "lives left") 
        print("Wrong letters: ",failed) 
        print(blankword)
        guess = input("Guess a letter from a-z: ") # asks user to guess a letter.           
        guess = guess.lower()
        
        if previous(previouss,guess):  # If the guess doesnt match any of the previous guesses run the code 
            failed = fail(failed)
        
            if guess == newword: #If the user puts in the answer, this will make it so that they instantly win. 
                print("You won!")
                print("Word:",newword, end= "")
                break    
        
            difference = letterInvestigator(guess, word, blankword, chances) # Sends the guess to the above method so that it can be related 
                                                                             # to the word, and replace the corerect letters,
                                                                             # if the guess is correct.
            chances = chance(chances,difference) # Updates the chances left
    
            if blankword == word: # If person completely fills the blank word with the correct 
                                  # letters, win message will be showed and the code ends.
                print("You won!")
                print("Word:",newword, end= "")
        else: # If guess matched one of the previous guesses, 
              # the following print statement will be stated.  
            print("You already guessed this letter")
        previouss = previouss + guess # space plus guess. 
        def image0():
            print ("+---+")
            print ("    |   ")
            print ("    |   ")  
            print ("    |   ")
            print ("    === ")
            return ("")
        def image1(): # Function for image by each stage. Self explanitory for the rest of these methods.
            print ("+---+")
            print (" O  |   ")
            print ("    |   ")  
            print ("    |   ")
            print ("    === ") 
            return ("")
        
        def image2():
            print ("+---+")
            print (" O  |   ")
            print (" |  |   ")  
            print ("    |   ")
            print ("    === ") 
            return ("")
        
        def image3():
            print ("+---+")
            print (" O  |   ")
            print ("/|  |   ")  
            print ("    |   ")
            print ("    === ") 
            return ("")
        
        def image4():
            print ("+---+")
            print (" O  |   ")
            print ("/|\ |   ")  
            print ("    |   ")
            print ("    === ") 
            return ("")
        
        def image5():
            print ("+---+")
            print (" O  |   ")
            print ("/|\ |   ")  
            print ("/   |   ")
            print ("    === ") 
            return ("")
        
        def image6():
            print ("+---+")
            print (" O  |   ")
            print ("/|\ |   ")  
            print ("/ \ |   ")
            print ("    === ") 
            return ("")
        if chances == 6:
            image0()
        if chances == 5:
            image1()
        if chances == 4:
            image2()
        if chances == 3:
            image3()  
        if chances == 2:
            image4()
        if chances == 1:
            image5()
        if chances == 0: #If the person runs out of lives, the game over message is shown.
            image6()
            print("Sorry!")
            print("The word was:",)
            print(newword)
            break
    start = input("Do you want to play again?(YES or NO)")