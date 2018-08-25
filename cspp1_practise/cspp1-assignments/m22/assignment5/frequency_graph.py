'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
Author : Praveen
Date : 25-08-2018
'''

def frequency_graph(dictionary):
    '''Sub Function'''
    li_st = sorted(list(dictionary.keys()))
    for lo_op in li_st:
        hash_string = ''
        for in_loop in range(dictionary[lo_op]):
            hash_string += '#'
        print(lo_op, "-", hash_string)

def main():
    '''Main Function'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
