'''
Author : Praveen
Date : 06-08-2018
'''
def eval_quadratic(input_a, input_b, input_c, input_x):
    '''This fuction evalute the Quadratic Expression'''
    return (input_a*(input_x**2))+(input_b*input_x)+input_c
def main():
    '''This is the main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    len_gth = len(data)
    for x_in in range(len_gth):
        temp = str(data[x_in]).split('.')
        if temp[1] == '0':
            data[x_in] = int(float(str(data[x_in])))
        else:
            data[x_in] = data[x_in]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
