'''
Author :Praveen
Date : 04-08-2018
'''
def main():
    '''
    THis function prints the product of digits in the given number
    '''
    int_input = int(input())
    if int_input < 0:
        fl_ag = 1
        int_input = abs(int_input)
    rem_inder = 0
    pro_duct = 1
    while int_input != 0:
        rem_inder = int_input % 10
        pro_duct = pro_duct * rem_inder
        int_input = int_input // 10
    if fl_ag == 1:
        print(0 - pro_duct)
    else:
        print(pro_duct)
if __name__ == "__main__":
    main()
