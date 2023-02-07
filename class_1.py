# 1
first = 7
second = 44.3
print(first + second)
print(first * second)
print(first / second)

# 2
a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8

print(f"a = {a}, b = {b}, c = {c}")

# 3
# There is no difference for Python between "john" and 'john'

# 4
my_number = 5 + 5
print(f"result is: {my_number}")

# 5
# The output will be 7 because we changed float y = 2.36 to int and it became 2

# 6
a = 8
b = "123"
print(a + int(b))

# Additional exercises
# 1
a = 5
b = 7
c = a
a = b
b = c
print(f"a = {a}, b = {b}")

# 2
a = 5
b = 7
a = a + b
b = a - b
a = a - b
print(f"a = {a}, b = {b}")

# 3
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
c = (a * a) + (b * b)
print(f"Sum of first and second numbers cubes: {c}")

# 4
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
c = int(input("Please enter the third number: "))
if a == b:
    print(a)
elif b == c:
    print(b)
elif c == a:
    print(c)
else:
    print("No equal nubmers there.")

# 5
numbers_list = []

first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))
third_number = int(input("Please enter the third number: "))

numbers_list.append(first_number)
numbers_list.append(second_number)
numbers_list.append(third_number)
numbers_list.sort()

print(f"The smallest number is {numbers_list[0]}")
