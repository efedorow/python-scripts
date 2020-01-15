# Develop a function `problem2(array1, array2)` with returns `True` if binary arithmetic operations (+, -, \*, etc) may be applied to the arrays `array1` and `array2`, `False` otherwise.

def problem2(array1, array2):
    if array1.ndim > array2.ndim:
        if array1.shape[-array2.ndim:]==array2.shape:
            return True
        else:
            return False
    elif array1.ndim < array2.ndim:
        if array2.shape[-array1.ndim:]==array1.shape:
            return True
        else:
            return False
    elif (array1.shape)==(array2.shape):
        return True
    else:
        return False
  
