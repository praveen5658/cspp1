'''
Author : Praveen
Date : 03-08-2018

'''
def square(x_input):
    '''
    Sub Function for computing Square of given number
    '''
    return x_input**2
def main():
    ''' This is the main fuction for computing Square of given number'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
