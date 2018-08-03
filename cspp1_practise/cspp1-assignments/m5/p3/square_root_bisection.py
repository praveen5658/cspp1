'''
Author : Praveen
Date : 03-08-2018

'''
def main():
    ''' This section tells square root of given number in Bisection method'''
    s_t = int(input())
    epsi_lon = 0.01
    lo_w = 0.0
    hi_gh = s_t
    an_s = (hi_gh + lo_w)/2.0
    while abs(an_s**2 - s_t) >= epsi_lon:
        if an_s**2 < s_t:
            lo_w = an_s
        else:
            hi_gh = an_s
        an_s = (hi_gh +lo_w)/2.0
    print(an_s)
if __name__ == "__main__":
    main()
