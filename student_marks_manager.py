
# Student Marks Manager

# Original list of student marks
original_marks = [75, 80, 65, 90, 85]

# Shared reference
shared_marks = original_marks

# Independent copy
copied_marks = original_marks.copy()

# Add a new mark to the copied list
copied_marks.append(95)

# Display the lists
print("Original marks:", original_marks)
print("Shared reference:", shared_marks)
print("Copied marks:", copied_marks)

# Compare identity and equality
print()
print("Original and shared reference are identical:", original_marks is shared_marks)

print("Original and copied lists have equal values:", original_marks == copied_marks)

print("Original and copied lists are identical:", original_marks is copied_marks)
