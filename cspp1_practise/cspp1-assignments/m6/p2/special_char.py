'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    str_final = ""
    length_str = len(str_input)
    for ch_ar in range(length_str):
        if str_input[ch_ar] in ('!', '@', '#', '$', '%', '^', '&', '*'):
            str_final += " "
        else:
            str_final += str_input[ch_ar]
    print(str_final)

if __name__ == "__main__":
    main()
