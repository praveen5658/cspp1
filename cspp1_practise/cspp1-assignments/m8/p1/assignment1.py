'''
Author : Praveen
Date : 07-08-2018
'''
def factorial(n):
    '''
    This function computes factorial of number using recursion
    '''
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
def main():
    a = input()
    print(factorial(int(a)))
if __name__ == "__main__":
    main()
