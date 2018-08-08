'''
Author : Praveen
Date : 08-08-2018
'''
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    cou = 0
    li_st1 = list(secret_word)
    li_st2 = list(secret_word)
    for va_r in letters_guessed:
        for va_r1 in li_st1:
            if va_r1 == va_r:
                li_st2.remove(va_r)
        if len(li_st2) is 0:
            cou = 1
            break
    return bool(cou)


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
        print(True)
    else:
        print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()
