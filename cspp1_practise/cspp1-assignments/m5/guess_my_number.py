'''
Author : Praveen
Date : 03-08-2018

'''
def main():
    '''This fenction guess the secret number '''
    print("Please think of a number between 0 and 100!")
    i = 0
    j = 100
    mid = (i+j)//2
    print("Is your secret number "+str(mid)+"?")
    print("Enter 'h' to indicate the guess is too high.")
    print("Enter 'l' to indicate the guess is too low.")
    print("Enter 'c' to indicate I guessed correctly.")
    s_t = input()
    while s_t != 'c':
        if s_t == 'l':
            j = mid
        elif s_t == 'h':
            i = mid
        else:
            print("Sorry, I did not understand your input.")
            print("Enter 'h' to indicate the guess is too high.")
            print("Enter 'l' to indicate the guess is too low.")
            print("Enter 'c' to indicate I guessed correctly.")
        mid = (i+j)//2
        print("Is your secret number "+str(mid)+"?")
        s_t = input()
    print("Game over. Your secret number was: "+str(mid))

if __name__ == "__main__":
    main()
