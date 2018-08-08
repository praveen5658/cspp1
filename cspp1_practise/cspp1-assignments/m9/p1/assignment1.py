'''
Exercise: Assignment-1
First, implement the function isWordGuessed that takes in two parameters -
a string, secret_word, and a list of letters, letters_guessed. This function
returns a boolean - True if secret_word has been guessed (ie, all the letters of
secret_word are in letters_guessed) and False otherwise.
'''


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    cou = 0
    l1 = list(secret_word)
    l2 = list(secret_word)
    for va_r in letters_guessed:
        for va_r1 in l1:
            if va_r1 == va_r: 
                l2.remove(va_r)
        if len(l2) == 0:
            cou = 1
            break
    if cou == 1:
        return True
    else:
        return False


def main():
    '''
    Main function for the program
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    if secret_word == "":
        return False
    else:
        print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()
