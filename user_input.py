#User input este de obicei tratat ca un string, indiferent daca introducem litere sau cifre

user = input("Please insert you name: ")
print("Hello ", user)
print("--------------------------------------------------------------------")

#other way
print(" Introduceti un cuvant: ")
user_input = input()
print("Ai introdus cuvantul: ", user_input)
print("--------------------------------------------------------------------")

#daca vrem ca un numar sa fie tratat ca un numar si nu ca un string
print("Enter the day number: ")
zi = int(input())
print ("Introduceti luna: ")
luna = input()
print("Introduceti anul: ")
an = int(input())
print("Data introdusa este: ", zi, "/", luna, "/", an)
print("--------------------------------------------------------------------")

number = int(input())
word = input()
song = number * word
print(song)

