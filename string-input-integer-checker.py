#find if an integer input is valid and return the integer from 1-500
def problem4(strinput):
    # Check for valid input and convert to integer type
    if strinput.isnumeric():
        intinput = int(strinput)
        # Check for valid integer value
        if 1 <= intinput <= 500:
            return intinput
        else:
            return None
    else:
        return None
