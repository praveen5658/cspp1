'''
Author : Praveen
Date : 06-08-2018
'''
def odd(input_x):
    '''
    Sub function returns False if given no is Odd and True otherwise
    '''
    return input_x%2 != 0
def main():
    '''This is the main function'''
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
