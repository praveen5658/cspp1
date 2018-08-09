'''
Author : Praveen
Date : 09-08-2018
'''

def get_available_letters(letters_guessed):
    '''
    This is sub function.
    '''
    data = list('abcdefghijklmnopqrstuvwxyz')
    for lo_op in letters_guessed:
        data.remove(lo_op)
    return ''.join(data)

def main():
    '''
    Main function
    '''
    user_input = input()
    user_input1 = user_input.lower()
    user_input2 = user_input1.split()
    data = []
    for char in user_input2:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
