'''
Author : Praveen
Date : 07-08-2018
'''
def iter_power(base, exp):
    '''
    FUnction for computing Power
    '''
    if exp == 0:
        return 1
    else:
        res_lt = 1
        for loop_vaiable in range(exp):
            res_lt *= base
            loop_vaiable += 1
        return res_lt
def main():
    '''This is main function'''
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
