#problem1
#Create a function that returns the factorial of a number. You should return None if there
#is an invalid input. Non-integer types and negative integer numbers are invalid input.
#The factorial of n is the product of the integers 1 to n.
#Note that 0! = 1.
#Example:
'''
4 -> 1x2x3x4 = 24
'''

# 5 Points
def problem2(n):
    # Check for valid input
    if type(n) == int:
        if n >= 0:
            # Start at 1 and keep multiplying by the next number until n is reached
            answer = 1
            for i in range(n):
                answer = answer*(i+1)
            return answer
        else:
            return None
    else:
        return None
