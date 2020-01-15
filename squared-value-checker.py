#find out if the squared value of one number is less than another number
def less_than_squared(a, b):
    #check that both inputs are floats
    if (type(a)==float) and (type(b)==float):
        #case 1: a^2 is less than b^2:
        if (a**2) < (b**2):
            return True
        #case 2: a^2 is greater than or equal to b^2:
        else:
            return False
    #if input is invalid, return None
    else:
        return None
