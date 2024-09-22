#w3 resource
#Sum all the items in a list

numbers_1 = [2,3,4,5,8]
numbers_3 = [2,3,4,5,8,9,19]
numbers_2 = [2,3,4,5]

def sum_numbers(list_item):
  total = 0
  for number in list_item:
    total += number
  return total

print(sum_numbers(numbers_1))

#pointers idea
# two pointers start in extreme and move to the center
def sum_numbers2(list_item):
  sum = 0
  count_down = -1
  if len(list_item) % 2 != 0:
    for index in range(len(list_item)//2):
      first = list_item[index]
      last = list_item[len(list_item) + count_down]
      count_down -= 1
      subtotal = first + last
      sum += subtotal
    sum += list_item[len(list_item)//2]
  return sum

print(sum_numbers2(numbers_1))

      




#generate list of numbers and swap to numbers by index