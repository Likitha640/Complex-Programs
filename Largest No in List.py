#Python Code for finding largest number in a list

# Function to find the largest number in a list
def find_largest_number(numbers):
    largest = float('-inf')  # Initialize largest as negative infinity
    
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest

# Function to sort a list in descending order using bubble sort
def bubble_sort_descending(numbers):
    n = len(numbers)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers

# Main program
if __name__ == '__main__':
    # Test the functions
    numbers = [10, 5, 8, 3, 2, 7, 1]
    
    largest_number = find_largest_number(numbers)
    sorted_numbers = bubble_sort_descending(numbers)
    
    print("The largest number is:", largest_number)
    print("The sorted list in descending order is:", sorted_numbers)