'''
    Author : Praveen
    Date : 17-08-2018
'''
import math
import copy
def remove_characters(input_string):
    '''
        removes extra charactes from input
    '''
    new_string = ''
    for lo_op in input_string:
        if 'a' <= lo_op <= 'z' or (lo_op == ' '):
            new_string += lo_op
    return new_string

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
    dict_common = {}
    dict1 = convert_dictionary(list1)
    dict2 = convert_dictionary(list2)
    product = 0
    sum_square1 = 0
    sum_square2 = 0
    for lo_op in dict1:
        if lo_op in dict2:
            dict_common[lo_op] = [dict1[lo_op]]
            dict_common[lo_op].append(dict2[lo_op])
        else:
            dict_common[lo_op] = [dict1[lo_op]]
            dict_common[lo_op].append(0)
    for lo_op in dict2:
        if lo_op not in dict_common:
            dict_common[lo_op] = [0]
            dict_common[lo_op].append(dict2[lo_op])
    d_i = copy.deepcopy(dict_common)
    for lo_op in d_i:
        le_n = len(lo_op)
        if le_n == 0:
            del dict_common[lo_op]
    for lo_op in dict_common:
        product += dict_common[lo_op][0]*dict_common[lo_op][1]
        sum_square1 += dict_common[lo_op][0]**2
        sum_square2 += dict_common[lo_op][1]**2
    return (product)/(math.sqrt(sum_square1) * math.sqrt(sum_square2))
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
