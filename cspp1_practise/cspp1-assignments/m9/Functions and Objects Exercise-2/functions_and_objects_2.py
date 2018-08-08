'''
Author : Praveen
Date : 08-08-2018
'''
def inc(i_n):
    '''This is incremention function'''
    return i_n+1

def apply_to_each(li_st, f_u):
    '''This is sub function'''
    lo_op = 0
    for va_r in map(f_u, li_st):
        li_st[lo_op] = va_r
        lo_op += 1
    print(li_st)

def main():
    '''This is main function'''
    data = input()
    data1 = data.split()
    list1 = []
    for va_r in data1:
        list1.append(int(va_r))
    apply_to_each(list1, inc)

if __name__ == "__main__":
    main()
