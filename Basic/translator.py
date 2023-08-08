
# Replacing the vowels with 'S' in a word

def translate (word) :
    vowel = "AEIOUaeiou"
    new_word = "" 

    for letter in word :
        # if letter.lower() in "aeiou" : 
        if letter in "AaEeIiOoUu" : 
            if letter.isupper() : 
                new_word += "S" 
            else : 
                new_word += "s" 
        else :
            new_word += letter

    return new_word  


s = input("Enter a word: ")
print ("New word: " + translate(s))


'''
ASme = A e -> S s
a e i o u
ofaubwhf aowufbuwo 
'''