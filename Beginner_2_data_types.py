# 1. Strings
print("Hello World")
print('i will learn Python and Java')

# 2. Numerical types
# int Eg: 11
print("type of variable 100 is:",type(100))

# float Eg: 11.0
print("type of variable 100.1 is:", type(100.1))
print(type(3.14))

numbers = ("1 2 3 4 5 6 7 8 9 10")      #1st solution
print("The printed numbers are:", numbers)

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)        #2nd solution

n=""        #ideal solution
for i in range(1, 11):
    n+=str(i) + " "
print("N Numbers are:", n)


#Quotes
#use double quotes if your string contains single quotes, for example, "You're doing great!"
#use single quotes if your string contains double quotes, for example, 'Have you read "Hamlet"?'
#Escaping: The backslash (\) will basically tell Python that the quote symbol that follows it is a part of the string rather than its end or beginning
print("You're doing great!")
print('You\'re doing greattttt!')

print("Have you read \"Hamleti\"?")
print('Have you read "Hamlet"?')
print("letter '\q\' is my favourite")
#print("\"canoodle" is a real word!")

#Multiline Strings: with triple quotes
print("""This
is
a
multi-line
string""")

print('''This
is
a
multi-line
string
that
matters''')

word1 = "King"
word2 = "Cross"
print(word1 + "'s " + word2)

