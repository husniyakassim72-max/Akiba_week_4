
# Question 1: Mutable and Immutable Objects

# Mutable example (List)
numbers = [10, 20, 30]

numbers.append(40)

print("List after modification:", numbers)

# Immutable example (String)
name = "Hana"

name = name + " Ali"

print("String after modification:", name)

# Question 2: References and Object Identity

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)
# question 3 :Shared References and Side Effects
numbers = [1, 2, 3]
values = numbers

values.append(4)

print(numbers)
print(values)
# Qeustion 4 :Function Arguments and Mutability
def update_lst(items):
    items.append(100)
scores=[50,60,70]
update_lst(scores)    
print(scores)
# Qeustion 5:
numbers = [10, 20, 30]

del numbers

print("Variable deleted")
# Does deleting one variable always destroy the object? 
numbers = [10, 20, 30]

values = numbers

del numbers

print(values)


# Question 5: Memory Management and Garbage Collection

numbers = [10, 20, 30]

values = numbers

print("Before deleting:", values)

del numbers

print("After deleting numbers:", values)
