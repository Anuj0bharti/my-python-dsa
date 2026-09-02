numbers = [10, 25, 7, 42, 18]  # Creating a list with n elements
                               # Time: O(1)

largest = numbers[0]           # Accessing the first element
                               # Time: O(1)

for number in numbers:         # Loop runs n times
                               # Time: O(n)
    if number > largest:       # Comparison happens n times
                               # Time: O(n)
        largest = number       # Runs at most n times
                               # Time: O(n)

print("Largest number:", largest)  # Runs once
                                   # Time: O(1)

# Overall Time Complexity: O(n)
# Because the list is traversed once.
