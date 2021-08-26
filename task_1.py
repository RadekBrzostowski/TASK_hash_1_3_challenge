def is_32bit_long_Int(x):
    if (-2147483648 <= x <= 2147483647):                        # check range of 32-bit long int.
        return(x)                                               # if pass return value
    else:
        return(0)                                               # if no-pass return 0


input_N = int(input("Input digit: "))                           # input value

# print(type(input_N))

if (is_32bit_long_Int(input_N) == 0):                           # check input
    print('0 - input')
else:
    output_N = int(''.join(reversed(str(abs(input_N)))))        # reverse string and convert to init
    if (input_N < 0):                                           # is input under 0
        output_N = -output_N
    if (is_32bit_long_Int(output_N) == 0):                      # check output
        print('0 - output')
    else:

        print(output_N)    
    
