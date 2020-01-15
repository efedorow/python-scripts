#check if an input is a palindrome (same backwards as forwards)
def problem5(palcheck):
    # Get rid of any differences in case
    palcheck = str(palcheck).lower()

    for i in range(len(palcheck)):
        # Check from end to begining
        # Could be faster by stopping the check at the middle but this still works
        if not (palcheck[-(i+1)]==palcheck[i]):
            return False
        else:
            return True
