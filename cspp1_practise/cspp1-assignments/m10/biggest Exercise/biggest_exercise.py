'''
Author :Praveen
Date : 09-08-2018
'''

def biggest(va_l):
    '''
    This is sub function
    '''
    su_m = 0
    if isinstance(va_l, (tuple, list)):
        for lo_op in va_l:
            if isinstance(lo_op, (tuple, list)):
                su_m += biggest(lo_op)
            else:
                su_m += 1
    else:
        su_m += 1
    return su_m

def main():
    '''aDict={}
    s=input()
    l=s.split()
    if l[0][0] not in aDict:
        aDict[l[0][0]]=[l[1]]
    else:
        aDict[l[0][0]].append(l[1])
    a_dict = {(1, 2):[1, 2, 3], 4:[9], 3:[9, 8], 'hello':'abcd'}
    This is main function
    '''
    a_dict = {(1, 2):[1, 2, 3, 5], 4:[[9, 0], 9], 3:[9, 8], 'hello':'abcd'}
    cou = 0
    for lo_op in a_dict:
        ret_urn = biggest(a_dict[lo_op])
        if cou < ret_urn:
            cou = ret_urn
            st_r = lo_op
    print(st_r)


if __name__ == "__main__":
    main()
