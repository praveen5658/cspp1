'''
Author : Praveen
Date : 08-08-2018
'''
def odd_tuples(input_tup):
    '''
    Function will print odd index values in tuple
    '''
    return input_tup[::2]
def main():
    '''This is main function'''
    data = input()
    data = data.split()
    a_tup = ()
    le_n = len(data)
    for j in range(le_n):
        a_tup += (int(data[j]),)
    print(odd_tuples(a_tup))
if __name__ == "__main__":
    main()
