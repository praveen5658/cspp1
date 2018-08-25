'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
Author : Praveen
Date : 25-08-2018
'''
def clean_string(string):
    '''Sub Function'''
    sample_string = ''
    for lo_op in string:
        if ('a' <= lo_op <= 'z' or
                'A' <= lo_op <= 'Z' or
                lo_op == ''):
            sample_string += lo_op
    return sample_string
def tokenize(string):
    '''Tokens the words'''
    dictionary = {}
    final_string = clean_string(string)
    li_st = final_string.split()
    for lo_op in li_st:
        if lo_op not in dictionary:
            dictionary[lo_op] = 1
        else:
            dictionary[lo_op] += 1
    return dictionary       
def main():
    '''Main Function'''
    string = ''
    num_ber = int(input())
    for lo_op in range(num_ber):
        string += input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
