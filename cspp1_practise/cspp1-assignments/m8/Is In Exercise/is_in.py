'''
Author : Praveen
Date : 07-08-2018
'''
LOW_VALUE = 0
HIGH_VALUE = 0
MID_VALUE = 0
def is_in(char, sort_str):
    '''
    This function returns 'True' if charaters present and 'False' if not
    '''
    global LOW_VALUE
    global HIGH_VALUE
    global MID_VALUE
    MID_VALUE = (LOW_VALUE + HIGH_VALUE) // 2
    if sort_str[MID_VALUE] == char:
        return 1
    elif MID_VALUE in (HIGH_VALUE, LOW_VALUE):
        return 0
    else:
        if sort_str[MID_VALUE] < char:
            LOW_VALUE = MID_VALUE
            return is_in(char, sort_str)
        HIGH_VALUE = MID_VALUE
        return is_in(char, sort_str)
def main():
    '''This is main function'''
    global LOW_VALUE
    global HIGH_VALUE
    global MID_VALUE
    data = input()
    data = data.split()
    char = data[0][0]
    input_string = data[1]
    sorted_string = ''.join(sorted(input_string))
    LOW_VALUE = 0
    HIGH_VALUE = len(sorted_string)
    MID_VALUE = 1
    print(is_in(char, sorted_string))


if __name__ == "__main__":
    main()
