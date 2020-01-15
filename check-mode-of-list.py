#Given a list of values, find the value that appears the most times in that list,
#return the value as well as its count.
#Assume that inputs are lists of either integers, strings, or a mix of both and that
#there are no lists which contain 2 values appearing an equal amount of times
#Output the values as given in the placeholder code

def problem7(valuelist):
    # Empty lists containing unique values and the their number of occurences
    uniques = []
    uniques_count = []

    for i in range(len(valuelist)):
        value = valuelist[i]
        if value in uniques:
            # Increment counter if already in uniques list
            uniques_count[uniques.index(value)] += 1
        else:
            # Add to uniques list and count with value of 1 if not already in unique list
            uniques.append(value)
            uniques_count.append(1)
    # Find the highest count value
    count = max(uniques_count)
    mode  = uniques[uniques_count.index(count)]

    return (mode,count)
