'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
Author : Praveen
Date: 25-08-2018
'''

def print_dictionary(dictionary):
    '''Sub Function'''
    li_st = sorted(list(dictionary.keys()))
    sample_dictionary = {}
    for lo_op in li_st:
        print(lo_op, "-", dictionary[lo_op])
def main():
    '''Main Function'''
    dictionary = eval(input())
    print_dictionary(dictionary)
if __name__ == '__main__':
    main()
