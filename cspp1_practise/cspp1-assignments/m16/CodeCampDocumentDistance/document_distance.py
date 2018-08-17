'''
    Author : Praveen
    Date : 17-08-2018
'''
import math
def remove_characters(input_string):
    '''
        removes extra charactes from input
    '''
    new_string = ''
    for lo_op in input_string:
        if (lo_op <= 'z' and lo_op >= 'a') or (lo_op == ' ') or (lo_op == "'"):
            new_string += lo_op
    return new_string
def frequency_sum(list1, list2):
    '''
        this will return frequency sum
    '''
    sum_digit1 = 0
    sum_square1 = 0
    sum_digit2 = 0
    sum_square2 = 0
    for lo_op in list1:
        sum_digit1 += lo_op
        sum_square1 += lo_op^2
    for lo_op in list2:
        sum_digit2 += lo_op
        sum_square2 += lo_op^2
    return sum_digit1, sum_square1, sum_digit2, sum_square2

def remove_stopwords(li_st, stop_words):
    '''
        remove stopd words from input
    '''
    li_st1 = li_st[:]
    for lo_op in li_st:
        if lo_op in stop_words:
            li_st1.remove(lo_op)
    return li_st1
def convert_dictionary(li_st):
    '''
        This will convert list into dictionary
    '''
    dictionary = {}
    for lo_op in li_st:
        if lo_op in dictionary:
            dictionary[lo_op] += 1
        else:
            dictionary[lo_op] = 1
    return dictionary

def similarity(list1, list2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = convert_dictionary(list1)
    dict2 = convert_dictionary(list2)
    list1_values = list(dict1.values())
    list2_values = list(dict2.values())
    (sum_digit1, sum_square1, sum_digit2, sum_square2) = frequency_sum(list1_values, list2_values)
    return (sum_digit1 * sum_digit2)/(math.sqrt(sum_square1) * math.sqrt(sum_square2))

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = (input().strip('\n')).lower()
    input2 = (input().strip('\n')).lower()
    string_1 = remove_characters(input1)
    string_2 = remove_characters(input2)
    input_list1 = string_1.split(" ")
    input_list2 = string_2.split(" ")
    stop_words = load_stopwords("stopwords.txt")
    final_list1 = remove_stopwords(input_list1, stop_words)
    final_list2 = remove_stopwords(input_list2, stop_words)
    print(similarity(final_list1, final_list2))

if __name__ == '__main__':
    main()