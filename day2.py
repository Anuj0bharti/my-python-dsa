numbers = [10, 20, 30, 40, 50]

# Get item: accessing by index
# Time Complexity: O(1)
print(numbers[2])


# Append: adding an element at the end
# Average Time Complexity: O(1)
numbers.append(60)


# Search: checking whether an element exists
# Time Complexity: O(n)
print(40 in numbers)


# Insert: adding an element in the middle
# Time Complexity: O(n)
numbers.insert(2, 25)


# Delete: removing an element
# Time Complexity: O(n)
numbers.remove(30)


# Iteration: visiting every element
# Time Complexity: O(n)
for number in numbers:
    print(number)


# Sort: arranging elements
# Time Complexity: O(n log n)
numbers.sort()

print(numbers)