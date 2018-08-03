'''
Author : Praveen
Date : 03-08-2018

'''
def main():
    ''' This section tells square root of given number in Newton- Rapson method'''
    in_put = int(input())
    epsi_lon = 0.01
    gu_ess = in_put/2.0
    while abs(gu_ess**2 - in_put) >= epsi_lon:
        gu_ess = gu_ess - (((gu_ess**2) - in_put)/(2*gu_ess))
    print(gu_ess)
if __name__ == "__main__":
    main()
