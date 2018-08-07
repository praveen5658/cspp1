'''
Author : Praveen
Date : 07-08-2018
'''
def factorial(input_n):
    '''
    This function computes factorial of number using recursion
    '''
    if input_n in (0, 1):
        return 1
    return input_n * factorial(input_n-1)
def main():
    '''This is main function'''
    input_a = input()
    print(factorial(int(input_a)))
if __name__ == "__main__":
    main()
