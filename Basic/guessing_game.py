secret_word = "Asme"
word = ""
limit = 3
i,j = 0,limit

while word != secret_word :
    if i < limit :    
        print ("    You have",j,"option left !!")
        word = input("Guess the word: ")
        i += 1
        j -= 1
    else :
        print ("You lose !!!")
        break 

if i < limit :
    print ("You win !!!")


###################################


out_of_guesses = False
i = 0

while word != secret_word and not out_of_guesses :
    if i < limit :    
        word = input("Enter the guessing word: ")
        i += 1

    else :
        out_of_guesses = True
        
if out_of_guesses :
    print ("You lose !!!")
else :
    print ("You win !!!")