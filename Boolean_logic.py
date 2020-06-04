is_open = True
is_closed = False
print (is_open)
print (is_closed)

#operatori booleani

            #AND = binary operator ; returns True if both arguments are true, otherwise, it returns False

a = True and True    # True
b = True and False   # False
c = False and False  # False
d = False and True   # False

           #OR = binary operator ; returns True if at least one argument is true, otherwise, it returns False.

a = True or True    # True
b = True or False   # True
c = False or False  # False
d = False or True   # True

           #NOT = unary operator ;  it reverses the boolean value of its argument.
to_be = True           # to_be is True
not_to_be = not to_be  # not_to_be is False

# prioritatile operanzilor booleani: not, and, or

# The operators "or" and "and" return one of their operands, not necessarily of the boolean type. Nonetheless, not always returns a boolean value.
truthy_integer = False or 5 and 100  # 100

tricky = not (False or '')  # True

                #Truthy and falsy values

#The following values are evaluated to False in Python:

# - constants defined to be false: None and False,
# - zero of any numeric type: 0, 0.0,
# - empty sequences and containers: "", [], {}.

# Logical operators in Python are short-circuited (Lazy).
# That means that the second operand in such an expression is evaluated only if the first one is not sufficient to evaluate the whole expression.

#x and y returns x if x is falsy; otherwise, it evaluates and returns y.
#x or y returns x if x is truthy; otherwise, it evaluates and returns y.

# division is never evaluated, because the first argument is True
lazy_or = True or (1 / 0)  # True

# division is never evaluated, because the first argument is False
lazy_and = False and (1 / 0)  # False

print ("exer1: ")
a = True
b = False
c = a and not b     #True  and not False = True and True => c = true

comp = a and (not c or b)
print(comp)     #false

#not None or 1  =  not False or True = True
