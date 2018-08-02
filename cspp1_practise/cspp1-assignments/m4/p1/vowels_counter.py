'''
Author : Praveen
Date : 02-08-2018

'''
def main():
    '''This function displays the number of vowels in the given string '''
    s_t = input()
    str_1 = "aeiou"
    co_u = 0
    for c_a in s_t:
        for c_1 in str_1:
            if c_a == c_1:
                co_u += 1
    print(co_u)

if __name__ == "__main__":
    main()
