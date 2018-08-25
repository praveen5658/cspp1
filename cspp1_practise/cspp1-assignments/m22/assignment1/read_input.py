'''
Write a python program to read multiple lines
of text input and store the input into a string.
Author : Praveen
Date : 25-08-2018
'''

def main():
    '''Main Function'''
    num_ber = int(input())
    for lo_op in range(num_ber):
        print(input())
        lo_op += 1
if __name__ == '__main__':
    main()
