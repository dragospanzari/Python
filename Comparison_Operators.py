#Comparison or relation operations let you compare two values and determine the relation between them.
#The result of applying these operators is always bool

# < strictly less than
# <= less than or equal
# > strictly greater than
# >= greater than or equal
# == equal
# != not equal
# is - object identity
# is not - negated object identity
# in - membership
# not in - negated membership.

a = 5
b = -10
c = 15

result_1 = a < b   # False
result_2 = a == a  # True
result_3 = a != b  # True
result_4 = b >= c  # False

calculated_result = a == b + c  # we basically check if 5 is equal to -10 + 15, which is true.

print("--------------------------------------------------------------------")
a = int(input().strip())

result = a > 0
print(result)
print("--------------------------------------------------------------------")
# The movie theater has N cinema halls that can accommodate K viewers each. Figure out if a movie theater can hold V viewers that plan to visit it on a particular day.
#
# The input format
#
# The first line is N cinema halls, the second line is their capacity (K), and the third line is the planned number of viewers (V).

cinema_halls = int(input())
capacity = int(input())
viewers = int(input())

supported = cinema_halls * capacity >= viewers
print(supported)

print("--------------------------------------------------------------------")
# Find out if the result of dividing A by B is an odd number.
#
# The input format:
#
# The first line is the dividend (A) and the second line is the divider (B). It is guaranteed that the numbers are divided without remainder.
#
# The output format:
#
# True or False

a = int(input())
b = int(input())
result = (a // b) % 2
print(result != 0)

print("--------------------------------------------------------------------")
#Write a program that reads an integer value from input and checks if it is less than 10 or greater than 250.
# Sample Input 1:
#
# 0
# Sample Output 1:
#
# True

a = int(input().strip())
print(a < 10 or a > 250)
