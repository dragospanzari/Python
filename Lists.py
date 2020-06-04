        # LIST = colectie din python

dog_breeds = ['dalmatian', 'caniche', 'vagabond']
print(dog_breeds)

numbers = [1, 2, 3, 4, 5]
print(numbers)

list_out_of_string = list ('pericol')       #creaza o lista cu elementele iterabile din obiectul declarat
print(list_out_of_string)

#String este un exemplu pt un obiect iterabil, iar int este exemplu de obiect neiterabil, de aceea mai jos nu va printa numerele din obiect
#list_out_of_integer = list(2356889)
#print(list_out_of_integer)

multi_element_list = list('elefantul')
print(multi_element_list)                   #va printa elementele din obiect separat

single_element_list = ["pericol"]
print("Elementul din obiect: ", single_element_list)                  #va printa obiectul

#de asemenea se pot crea liste goale cu [] si list
empty_list_1 = list()
empty_list_2 = []

#listele pot stoca valori duplicate
on_off_list = ['on','off','on', 'off']
print(on_off_list)

#lungimea unei liste

print("Numarul de elemente din lista 'dog_breeds' este de: ", len(dog_breeds))
print("Numarul de elemente din lista 'numbers' este de: ", len(numbers))
print(len(empty_list_1))
print("Numarul de elemente din lista iterabila de tip String este de: " , len(multi_element_list))

