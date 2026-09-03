
# DSA with Python

This repository contains my daily practice and learning of Data Structures and Algorithms using Python.

## Day 1

### Topic Covered

Time Complexity

Time complexity is used to understand how the running time of a program grows with the input size.

### Practice

Solved problems to find and understand their time complexity.

```python
numbers = [10, 25, 7, 42, 18]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)
```

Time Complexity: **O(n)**

The loop checks every element in the list once, so for `n` elements it runs `n` time

## Day 2

### Topic Covered

TLE (Time Limit Exceeded)

TLE occurs when a program takes more time than the allowed limit to execute.

Python List Time Complexity

Learned the time complexity of common Python list operations.

### Practice

Studied the time complexity of Python list operations and practiced identifying operations that can lead to TLE.

| Operation | Time Complexity |
|---|---|
| Copy | O(n) |
| Append | O(1) |
| Pop last | O(1) |
| Pop intermediate | O(n) |
| Insert | O(n) |
| Get Item | O(1) |
| Set Item | O(1) |
| Delete Item | O(n) |
| Iteration | O(n) |
| Get Slice | O(k) |
| Delete Slice | O(n) |
| Set Slice | O(k+n) |
| Extend | O(k) |
| Sort | O(n log n) |
| Multiply | O(nk) |
| Search (`x in s`) | O(n) |
| min(), max() | O(n) |
| Get Length | O(1) |

Practice code: `day2.py`

### Notes
