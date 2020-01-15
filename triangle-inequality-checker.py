#check if a triangle follows the triangle inequality theorem and return an integer corresponding to 1,2,3
#based on whether it is isoceles, equilateral or scalene
def problem6(a,b,c):
    # Check if it isnt valid
    if not ((a + b > c) and (a + c > b) and (b + c > a)):
        return None
    else:
        # Check number of sides that equal each other
        if ((a == b) and (b == c)):
            return 1
        elif ((a == b) or (b == c) or (c == a)):
            return 2
        else:
            return 3
