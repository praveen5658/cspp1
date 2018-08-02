'''
Author : Praveen
Date : 02-08-2018

'''
def main():
    '''This program displays the largest alphabetical sequence in the given string'''
    st_r = input()
    st_r1 = st_r[0]
    ma_x = 0
    co_u = 0
    for i_v in range(len(st_r)-1):
        if st_r[i_v] < st_r[i_v+1]:
            co_u += 1
            st_r1 += st_r[i_v+1]
        else:
            if ma_x <= co_u:
                ma_x = co_u
                st_r2 = st_r1
            co_u = 0
            st_r1 = st_r[i_v+1]
    if co_u > ma_x:
        st_r2 = st_r1
    print(st_r2)


if __name__ == "__main__":
    main()
