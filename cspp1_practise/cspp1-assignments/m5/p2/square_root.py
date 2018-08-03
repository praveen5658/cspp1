'''
Author : Praveen
Date : 03-08-2018

'''
def main():
    ''' This section tells square root of given number in Approximation method'''
    s_t = int(input())
    epsi_lon = 0.01
    gu_ess = 0.0
    incre_ment = 0.1
    while abs(gu_ess**2 - s_t) >= epsi_lon:
        if gu_ess <= s_t:
            gu_ess += incre_ment
        else:
            break
    if abs(gu_ess**2 - s_t) >= epsi_lon:
        print(" Failed to compute Square root of given number")
    else:
        print(gu_ess)
if __name__ == "__main__":
    main()
