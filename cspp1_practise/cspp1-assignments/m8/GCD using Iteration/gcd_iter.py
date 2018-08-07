'''
Author : Praveen
Date : 07-08-2018
'''
def gcd_iter(input_a, input_b):
    '''
    This function returns GCD of given two numbers
    '''
    if input_a < input_b:
        input_a, input_b = input_b, input_a
    while input_b > 0:
        if input_a%input_b == 0:
            break
        else:
            input_c = input_a
            input_a = input_b
            input_b = input_c % input_a
    return input_b
def main():
    '''THis is main function'''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
