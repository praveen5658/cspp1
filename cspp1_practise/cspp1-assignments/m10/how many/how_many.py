'''
Author : Praveen
Date : 09-08-2018
'''


def how_many(va_l):
    '''
    This is sub function
    '''
    su_m = 0
    for lo_op in va_l:
        if isinstance(lo_op) in (tuple, list):
            su_m += how_many(lo_op)
        else:
            su_m += 1
    return su_m

def main():
    '''nu_m=input()
    a_dict={}
    for lo_op in range(int(nu_m)):
        st_r=input()
        li_st=st_r.split()
        if li_st[0] not in a_dict:
            a_dict[li_st[0]]=[li_st[1]]
        else:
            a_dict[li_st[0]].append(li_st[1])
    This is main function'''
    a_dict = {(1, 2):[1, 2, 3], 4:[9], 3:[9, 8], 'hello':'abcd'}
    va_l = list(a_dict.values())
    print(how_many(va_l))


if __name__ == "__main__":
    main()
