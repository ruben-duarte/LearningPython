#Remover duplicados de Array ordenado

arr = [1,2,2,3,4,4,5,5,5]

# crear otro array y colocar los elementos no repetidos
unique_elements = []

# revisa si el siguiente elemento no es igual al anterior hasta penultimo elemento
for i in range(len(arr)-1):
  if arr[i] != arr[i+1]:
    unique_elements.append(arr[i])
    #inserta el elemento y avanza al siguiente item
  #inserta el ultimo elemento 
unique_elements.append(arr[i+1])

print(unique_elements)


