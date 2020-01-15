#Given an input of a set of lists, convert this set into a matrix where
#the first list is the first row, the second list is the second row, and so on.
#Return None if a valid matrix cannot be made (empty rows or rows of varying lengths),
#return True if the matrix is invertible and return False if the matrix is valid but not invertible
#You can assume that the lists all contain only floating point numbers and that you are given at least
#2 lists each time

def problem8(setoflists):
    # Set a list length that all lists must meet based on first list passed
    listlength = len(setoflists[0])
    # Check that all lists are of this length
    for i in range(1,len(setoflists)):
        if listlength != len(setoflists[i]):
            return None
    # Check if it is a square matrix
    if len(setoflists) != listlength:
        return None
    else:
        # Create a matrix of these lists and check its determinant is more than 0 (1e-6 for float tolerance)
        A = array(setoflists)
        A = matrix(A)
        if (abs(linalg.det(A)) > 1e-6):
            return True
        else:
            return False
