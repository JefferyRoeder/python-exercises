import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1 Negative numbers

negative_numbers = a[a < 0]
print(negative_numbers)
#2 positive numbers

positive_numbers = a[a > 0]
print(positive_numbers)

#3 Even and positive numbers

even_and_positive = np.logical_and(a > 0, a % 2 == 0)
a[even_and_positive]

print(even_and_positive)

#4 If you were to add 3 to each data point, how many positive numbers would there be?

a_plus_3 = a + 3

a_plus_3_positive = a_plus_3[a_plus_3 > 0]

print(a_plus_3_positive)

#5 If you squared each number, what would the new mean and standard deviation be?
a_squared = a**2
print(a_squared.std())

#6 A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.
a_centered = a - a.mean()
print(a_centered)

# calc z score

a_zscore = (a - a.mean())/a.std()


# additional exercises


# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum_of_a / len(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

def multiply_list(my_list):
    result = 1
    for i in my_list:
        result = result * i
    return result

print(multiply_list(a))

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
def square_list(my_list):
    new_list = []
    for i in my_list:
        new_list.append(i **2)
    return new_list

print(square_list(a))

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
def odds_only(my_list):
    new_list = []
    for i in my_list:
        if i % 2 == 1:
            new_list.append(i)
    return new_list

print(odds_only(a))

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
def evens_only(my_list):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print(evens_only(a))


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

print(b.sum())

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
b.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
b.max()


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))
b.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
b.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = b ** 2
# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b = b[b % 2 == 1]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b = b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.
print(b.shape())
# Exercise 10 - transpose the array b.
b.transpose()
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b_reshape = b.reshape(1,6)
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b_reshape2 = b.reshape(6,1)


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c.min()
c.max()
c.sum()
c.prod()

# Exercise 2 - Determine the standard deviation of c.
c.std()

# Exercise 3 - Determine the variance of c.
c.var()
# Exercise 4 - Print out the shape of the array c
c.shape()
# Exercise 5 - Transpose c and print out transposed result.
print(c.transpose())
# Exercise 6 - Multiply c by the c-Transposed and print the result.
print(c * c.transpose())
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
(c * c.transpose()).sum()
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
(c * c.transpose()).prod()

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
# Exercise 4 - Find all the negative numbers in d
d[d %]
# Exercise 5 - Find all the positive numbers in d
positive_numbers_d = d[d > 0 ]
# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
# Exercise 8 - Print out the shape of d.
d.shape()
# Exercise 9 - Transpose and then print out the shape of d.
np.shape(d)
# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)