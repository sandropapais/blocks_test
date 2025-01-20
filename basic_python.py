def sort_array(arr):
    """
    Sorts an array in ascending order.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new list with the elements sorted in ascending order.
    """
    if not isinstance(arr, list):
        raise ValueError("Input must be a list.")

    return sorted(arr)

# Example usage
if __name__ == "__main__":
    sample_array = [5, 2, 9, 1, 5, 6]
    print("Original array:", sample_array)
    sorted_array = sort_array(sample_array)
    print("Sorted array:", sorted_array)
