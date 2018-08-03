'''
Author : Praveen
Date : 03-08-2018

'''
def main():
    ''' This section tells that given number is perfect cube or not in Guess and Check method'''
    s_t = int(input())
    i_t = 0
    co_u = 0
    while i_t <= s_t:
        if i_t**3 == s_t:
            print(str(s_t)+" is a perfect cube")
            co_u = 1
            break
        i_t += 1
    if co_u == 0:
        print(str(s_t)+" is not a perfect cube")
if __name__ == "__main__":
    main()
