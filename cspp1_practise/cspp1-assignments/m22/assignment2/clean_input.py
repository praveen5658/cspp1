'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
Author : Praveen
Date : 25-08-2018
'''

def clean_string(string):
    '''Sub Function'''
    sample_string = ''
    for lo_op in string:
        if ('a' <= lo_op <= 'z' or
           'A' <= lo_op <= 'Z' or
           '0' <= lo_op <= '9'):
            sample_string += lo_op
    return sample_string

def main():
    '''Main Function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
