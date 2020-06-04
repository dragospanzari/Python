print(10+5)
print(100-10)
print (77/10)
print (77//10)      #integer division ignores the decimal part

print (2+2*2)
print((2+2)*2)
print(-10*10)
print (100**2)      #ridicarea la putere
print(2**3)

# The remainder of a division  Applied to 2, it returns 1 for odd numbers and 0 for the even ones.
print(7 % 2)  # 1, because 7 is an odd number
print(8 % 2)  # 0, because 8 is an even number

#modulo operator % is used to get remainder of a division; the remainder always has the same sign as the divisor.
# Divide the number by itself
print(4 % 4)     # 0
# At least one number is a float
print(11 % 6.0)  # 5.0
# The first number is less than the divisor
print(55 % 77)   # 55
# With negative numbers, it preserves the divisor sign
print(-11 % 5)    # 4
print(11 % -5)    # -4

#prioritatile operatiilor matematice: paranteze, putere, unuary minus, inmultire, impartire, remainder, adunare, scadere


print ("ex 1")
a = int(input())
b = int(input())
c = int(input())
math = a * b - c
print(math)

print ("ex 2")
n = int(input())
add = n + n
mult = add * n
minus = mult - n
remain = minus // n
print (remain)

#simplificat, exercitiul 2 arata asa:
n = int(input())
math = ((((n + n) * n) - n) // n)
print (math)

