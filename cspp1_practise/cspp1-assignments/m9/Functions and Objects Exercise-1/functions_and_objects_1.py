'''
Author : Praveen
Date : 08-08-2018
'''
def apply_to_each(li_st, f_u):
    '''This is sub function'''
    le_n = len(li_st)
    for va_r in range(le_n):
        li_st[va_r] = f_u(li_st[va_r])
    print(li_st)

def main():
    '''This is main function'''
    data = input()
    data1 = data.split()
    list1 = []
    for va_r in data1:
        list1.append(int(va_r))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()
