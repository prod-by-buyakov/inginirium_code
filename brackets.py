def check_string_brackets(input_string):
    open=0
    close=0
    for s in input_string:
        if "(" in s:
            open+=1
        else:
            close+=1
    if open == close:
        print('yes')
    else:
        print('no')

check_string_brackets(")(")