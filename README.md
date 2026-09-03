
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

Day 2
Topics Covered

TLE (Time Limit Exceeded)

TLE occurs when a program takes longer than the allowed time limit to execute. Efficient algorithms help avoid TLE for large inputs.

Python List Time Complexity

Learned the time complexity of common Python list operations such as append, pop, insert, delete, slicing, searching, sorting and iteration.

Practice

Studied the time complexity of Python list operations.

Append       O(1)
Pop last     O(1)
Get item     O(1)
Set item     O(1)
Iteration    O(n)
Search       O(n)
Insert       O(n)
Delete       O(n)
Sort         O(n log n)
Get length   O(1)
