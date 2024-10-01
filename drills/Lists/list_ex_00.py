# interchange first and last elements in a list
# Given a list, write a Python program to swap the first and last element of the list

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 4, 5]
my_list3 = [1, 2, 3, 4, 5]

def swap_first_and_last(data):
    no_swap = (data[0], data[-1])
    data[0] = no_swap[1]
    data[-1] = no_swap[0]
    return data

new = swap_first_and_last(my_list1)
print(new)


a, b = (2,3)
print(a,b)
(b,a) = (a,b)
print(a,b)

def swap_2(list_data):
    a, b = list_data[0], list_data[-1]  # Obtienes el primer y último elemento
    list_data[0] = b  # Realizas el swap directamente en la lista
    list_data[-1] = a
    return list_data

new_2 = swap_2(my_list2)
print("swap 2")
print(new_2)

def swap_3(list_data):
    a, b = list_data[0], list_data[-1]  # Obtienes el primer y último elemento
    p, q = b, a 
    list_data.pop()
    list_data.append(q)
    list_data.pop(0)
    list_data.insert(0,p)
    return list_data

new_3 = swap_3(my_list3)
print("swap 3")
print(new_3)
