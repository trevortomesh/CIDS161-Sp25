# Lists and Indices in Python

## Summary

This lecture introduces students to Python's list data structure as a solution to managing multiple variables. It contrasts traditional variable-by-variable handling with the flexibility of lists. Key list operations, indexing behavior, and their differences from Java arrays are explored through hands-on examples.

---

## Why Lists?

In early programming, handling several related values (like a list of ages) requires declaring multiple variables:

```python
age1 = 36
age2 = 22
age3 = 23
...
```

To compute something like the average, you'd need to manually add them up:

```python
average = (age1 + age2 + age3 + ...) / number_of_ages
```

This becomes impractical for large data sets.

### Solution: Lists

A **list** is a sequence that stores multiple items in a single variable.

```python
ages = [36, 22, 23, 21, 19, 21, 51, 32]
```

This allows operations like:

```python
average = sum(ages) / len(ages)
```

## Key List Concepts

### Indexing (0-based)

Python lists are **0-indexed**, meaning the first element is accessed with index 0:

```python
print(ages[0])  # 36
```

To access the last element:

```python
print(ages[len(ages) - 1])  # 32
```

Using an index equal to `len(ages)` will produce an **IndexError**:

```python
print(ages[8])  # IndexError: list index out of range
```

### Negative Indexing

Python supports negative indices:

```python
print(ages[-1])  # 32 (last element)
```

### Common List Functions

* `len(list)`: Number of elements
* `sum(list)`: Sum of numeric elements
* `max(list)`: Largest element
* `min(list)`: Smallest element

### Element Access and Assignment

Elements can be changed using their index:

```python
ages[0] = 42
```

### Looping Through a List

Using a loop to access or modify elements:

```python
for i in range(len(ages)):
    print(f"Index {i} has value {ages[i]}")
```

You can also assign new values:

```python
for i in range(len(ages)):
    ages[i] = i
```

### Summary Example

```python
ages = [36, 22, 23, 21, 19, 21, 51, 32]
print("Average age:", sum(ages) / len(ages))
print("Youngest:", min(ages))
print("Oldest:", max(ages))
print("Age range:", max(ages) - min(ages))
```

## Comparison to Java Arrays

* Python lists are flexible and dynamic.
* Java arrays are fixed in size and have stricter type constraints.
* In Java, printing an array directly doesn't show values; it shows a memory reference. Python is more intuitive for beginners in this regard.

## Practice Questions

1. What will `ages[-2]` return?
2. How do you replace the third element of a list with `99`?
3. What does `len([5, 6, 7, 8])` return?
4. Write a loop that prints only even-indexed elements.
5. How would you safely access the last element of a list without hardcoding the index?

---

This lesson builds foundational understanding of lists, preparing students for deeper collection-based programming in future courses like CS 162.
