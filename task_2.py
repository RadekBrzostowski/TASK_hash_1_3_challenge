# PYTHON 3.xx
dict_keynum = {
    '0': ['@'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


input_digits = input("Enter digits: ")

if input_digits.isdigit():
    input_digits = int(input_digits)
    list_digits=[]
    list_digits[:0]=str(input_digits)                       # digits in list as string
    out_this2 = []                                          # output list 
    out_temp = []                                           # temporary list


    for x in list_digits:
        out_this = [b for a, b in dict_keynum.items() if x == a]        # list from dictionary
        for d in out_this:
            if out_this2 == []:
                out_temp = d
            else:
                for e in out_this2:
                    for f in d:
                        out_temp.append(e+f)
        out_this2 = out_temp
        out_temp =[]
    print(out_this2)                    
elif input_digits == "":
    out_this2 = []
    print(out_this2)
else:
    print("Please input only digits.")
    

# print("Len ", len(out_this2))