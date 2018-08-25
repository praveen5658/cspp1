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
                '0' <= lo_op <= '9' or
                lo_op == ' '):
            sample_string += lo_op
    return sample_string
def tokenize(string):
    '''Tokens the words'''
    dictionary = {}
    final_string = clean_string(string)
    # print(final_string)
    li_st = final_string.split()
    le_n = len(li_st)
    for lo_op in range(le_n):
        if li_st[lo_op] not in dictionary:
            dictionary[li_st[lo_op]] = 1
        else:
            dictionary[li_st[lo_op]] += 1
    return dictionary
def main():
    '''Main Function'''
    string = ''
    num_ber = int(input())
    for lo_op in range(num_ber):
        string += input()
        string += ' '
        lo_op += 1
    print(tokenize(string))

if __name__ == '__main__':
    main()
