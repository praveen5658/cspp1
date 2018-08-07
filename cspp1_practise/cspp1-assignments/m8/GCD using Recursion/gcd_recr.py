'''
Author : Praveen
Date : 07-08-2018
'''
def gcd_recur(input_a, input_b):
    '''
    This function returns GCD of two numbers using Recursion
    '''
    if input_a < input_b:
        input_a, input_b = input_b, input_a
    if input_a % input_b == 0:
        return input_b
    return gcd_recur(input_b, input_a % input_b)
def main():
    '''This is main function'''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
