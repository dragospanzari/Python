#indexes are used to access elements within a sequence. they start from 0
#indexes of elements
colors = ['red','green', 'blue','yellow']
print(colors[0])        #printeaza elementul 0 din lista, care este red

pet = "dog"
print(pet[2])       #printeaza indexul 2 al cuvantului 'dog' care este "g"

#putem modifica indecsii dintr-o lista cu noi valori
colors[1] = "purple"
print("Noua lista va fi: ", colors)

#nu putem modifica indecsii dintr-un string
pet1 = "camel"
#pet1[0] = "b" # eroare

#indecsii negativi acceseaza ultimul element dintr-o lista
print("ultima culoare din lista este: ", colors[-1])
print("penultima culoare din lista este: ", colors[-2])

