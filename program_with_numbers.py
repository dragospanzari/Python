# variable = input()                       #String
# integer = int(input())                  #Integer
# floating_point = float(input())         #Float

# the average amount of money per month
money = int(input("How much money do you spend per month: "))

# the number of miles per piece of money
n_miles = 2

# earned miles
miles_per_month = money * n_miles

# the distance between London and Paris
distance = 215

# how many months do you need to get
# a free trip from London to Paris and back
print("in ", distance * 2 / miles_per_month, "months you need to get a free trip from London to Paris and Back")

print("--------------------------------------------------------------------")

#advanced forms of assignement
# simple assignment
number = 10
number = number + 1  # 11
#sau
number += 1  # 11

print("--------------------------------------------------------------------")
counter = 10
step = int(input())  # let it be 3
counter += step
print("Counter + step: ", counter)  # it should be 13, then

print("--------------------------------------------------------------------")
#Ask the user about parameters of a rectangular parallelepiped (3 integers representing the length, width and height)
# and print the sum of edge lengths, its total surface area and volume.

a = int(input())
b = int(input())
c = int(input())

sum_of_legths = 4*(a+b+c)
print(sum_of_legths)
surface_area = 2*(a*b + b*c + a*c)
print(surface_area)
volume = a * b * c
print(volume)

print("--------------------------------------------------------------------")
#For the given amount of money, calculate the income from this savings account with a 5% interest rate after one year.
# Save the result into the variable income.

amount = 1000
interest_rate = 5
years = 1
# change the next line
income = (amount * interest_rate * years) / 100

print("--------------------------------------------------------------------")
# A school has decided to create three new math groups and equip three classrooms for them with new desks. At most two students may sit at any desk. The number of students in each of the three groups is known. Output the smallest amount of desks to be purchased.
# Each group will sit in its own classroom.
# The program receives the input of three non-negative integers: the number of students in each of the three classes (the numbers do not exceed 1000).
#
print("Introduceti nr de studenti din prima grupa: ")
group_1 = int(input())
print("Introduceti nr de studenti din a doua grupa: ")
group_2 = int(input())
print("Introduceti nr de studenti din a treia grupa: ")
group_3 = int(input())

nr_studenti = group_1 + group_2 + group_3
nr_banci = (nr_studenti // 2) + (nr_studenti % 2)
print("Pentru un numar total de ", nr_studenti, "este nevoie de ",nr_banci, "banci")

        # alta varianta
# group_1 = int(input())
# birouri_1 = (group_1 // 2) + (group_1 % 2)
# group_2 = int(input())
# birouri_2 = (group_2 // 2) + (group_2 % 2)
# group_3 = int(input())
# birouri_3 = (group_3 // 2) + (group_3 % 2)
# nr_banci = birouri_1 + birouri_2 + birouri_3
# print(nr_banci)




