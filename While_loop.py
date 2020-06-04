number = 0
while number < 5:
    print(number)
    number += 1
print('Now: equal to 5')

print("---------------------------------------------------------------------------------------------------------------------")
x = 25
# while x % 2 != 0:     #1 numar
#     print(x)
#     x += 3

while x <= 30:        #2 numere
    print(x)
    x += 3

# while x*2 % 100 >= 50:     #9 numere
#     print(x)
#     x += 3

# while x > 0:          #infinit
#     print(x)
#     x += 3
print("---------------------------------------------------------------------------------------------------------------------")
number = 0
while number < 12:
   print(number)
   number += 2

print("---------------------------------------------------------------------------------------------------------------------")
#What is the value of "i" at the end of the program?
i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
print(i)

print("---------------------------------------------------------------------------------------------------------------------")
# Write a program that prints all even numbers less than the input number using the while loop.
# The input format:
# The maximum number N that varies from 1 to 200.
# The output format:
# All even numbers less than N in ascending order. Each number must be on a separate line.

        #toate numerele pare pana la 200
# i = 1
# while i <= 200:
#     i = i + 1
#     if i % 2 == 0:
#         print(i)
i = 1
n = int(input())
while i < n:
    # i = i + 1
    # if i % 2 == 0 and i < n:
    #     print(i)       #toate numerele pare pana la cifra introdusa
    if i %2 == 0:
        print(i)
    i +=1
