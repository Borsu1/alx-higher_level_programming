#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Function to find a peak in a list  of unsorted integers.
    
    Args:
        list_of_integers (list): The list of integers.

    Returns:
        int: A peak in the list of integers. If the list is empty, returns None.

        This function uses a binary search approach to find a peak in the list.
        The time complexity of this function is 0(log n), where n is the length of      list.
        Note that this function returns the first peak it finds, not necessarily t  he highest peak or all peaks.
        """
        # Check if the list is empty
        if not list_of_integers:
            return None

        low = 0
        high = len(list_of_integers) - 1

        # Use binary search to find a peak
        while low < high:
            mid = (low + high) // 2
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                high = mid
            else:
                low = mid + 1

                return list_of_integers[low]
