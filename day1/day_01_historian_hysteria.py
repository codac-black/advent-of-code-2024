def read_input_file(filename):
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            # Split the line into two numbers
            numbers = line.split()
            if len(numbers) == 2:
                left_list.append(int(numbers[0]))
                right_list.append(int(numbers[1]))

    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    """
    Calculate the total distance between corresponding elements of two lists.
    This function sorts both input lists and then calculates the sum of the 
    absolute differences between corresponding elements of the sorted lists.
    Args:
        left_list (list of int/float): The first list of numbers.
        right_list (list of int/float): The second list of numbers.
    Returns:
        int/float: The total distance between corresponding elements of the two lists.
    Raises:
        ValueError: If the input lists are not of equal length.
    """
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    if len(left_sorted) != len(right_sorted):
        raise ValueError("Lists must be of equal length 😥")
    # Calculate the total distance
    total_distance = sum(abs(left - right)
                         for left, right in zip(left_sorted, right_sorted))

    return total_distance


# Example usage
filename = 'input.txt'
left_list, right_list = read_input_file(filename)
# Calculate and print the total distance
total_distance = calculate_total_distance(left_list, right_list)
print("Puzzle solution 🌚:", total_distance)
