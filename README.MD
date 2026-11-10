### Question 1: Mutable and Immutable Objects
Mutable objects can be changed after they are created. For example, a list is mutable because we can add, remove, or update its elements.

Immutable objects cannot be changed after they are created. For example, a string is immutable. When we combine a string with another string, Python creates a new string instead of changing the original one.

## Program output:
List after modification: [10, 20, 30, 40]
String after modification: Hana Ali### Question 2: References and Object Identity

**1. What is the output?**
***True
***False
***True


**2. Explain the difference between `is` and `==`.**

The `is` operator checks whether two variables refer to the same object in memory. The `==` operator checks whether two objects have equal values.

**3. Why do a and c have the same values but different identities?**

Because Python creates two separate list objects. Both lists contain [10, 20, 30], but they are stored as different objects in memory. Therefore, `a == c` is True, but `a is c` is False.
 ### Question 4: Function Arguments and Mutability

**1. What is the output?**

```text
[50, 60, 70, 100]
```

**2. Explain why the original list changes after the function call.**

The original list changes because Python passes a reference to the same list object to the function. The parameter `items` refers to the same object as `scores`. When the function uses `append(100)`, it modifies the original list.

**3. Modify the function so that it creates and returns a new list.**

```python
# def update_list(items):
#     new_list = items.copy()
#     new_list.append(100)
#     return new_list

# scores = [50, 60, 70]

# new_scores = update_list(scores)

# print("Original:", scores)
# print("New list:", new_scores)
```

**Output:**

```text
Original: [50, 60, 70]
New list: [50, 60, 70, 100]
```

The `copy()` method creates a separate list, and `return` sends the new list back without changing the original list.
### Question 5: Memory Management and Garbage Collection

**1. How does Python manage objects in memory and how does garbage collection work?**

Python creates objects in memory when we use them. Variables hold references to these objects. Python uses reference counting and garbage collection to manage memory and clean up objects that are no longer needed.

**2. What happens when `del` is used?**

The `del` statement removes a variable reference. It does not necessarily destroy the object itself.

**3. Does deleting one variable always destroy the object?**

No. If another variable still refers to the same object, the object remains available.

**4. What happens when an object is no longer referenced?**

The object becomes eligible for garbage collection, and Python can reclaim its memory.
## Practical Mini-Project: Student Marks Manager

### Project Reflection

**1. Why does modifying a shared reference affect the original list?**

Because both variables refer to the same list object in memory. When we modify the list using one variable, the changes are visible through the other variable.

**2. Why does modifying the copied list not affect the original list?**

Because the `copy()` method creates a separate list object. Changes made to the copied list do not affect the original list.

**3. What is the difference between equality and identity in Python?**

Equality (`==`) checks whether two objects have the same values. Identity (`is`) checks whether two variables refer to the same object in memory.