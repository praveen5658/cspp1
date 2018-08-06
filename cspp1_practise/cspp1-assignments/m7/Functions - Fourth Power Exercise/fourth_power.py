'''
Author : Praveen
Date : 06-08-2018
'''
def square(input_x):
    '''
    This function computes square of value
    '''
    return input_x*input_x
def fourth_power(input_x):
    '''
    This function computes Fourth poer of value
    '''
    return square(square(input_x))
def main():
    '''This is the main function'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data)))))
    else:
        print(fourth_power(data))

if __name__ == "__main__":
    main()
