'''
Author : Praveen
Date : 02-08-2018

'''
def main():
    '''This fenction displays the number of times "bob" present in the given string'''
    s_t = input()
    co_u = 0
    for i in range(len(s_t)-2):
        if s_t[i:i+3] == 'bob':
            co_u += 1
            i += 2
    print(co_u)

if __name__ == "__main__":
    main()
