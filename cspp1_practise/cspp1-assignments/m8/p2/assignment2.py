'''
Author : Praveen
Date : 07-08-2018
'''
def sumof_digits(input_n):
    '''
    This function computes sum of individual digits
    '''
    if input_n == 0:
        return 0
    return input_n % 10 + sumof_digits(input_n // 10)
def main():
    '''This is main function'''
    input_a = input()
    print(sumof_digits(int(input_a)))
if __name__ == "__main__":
    main()
