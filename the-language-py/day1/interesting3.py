# >>> basket = ['a','b','r','c']
# >>> basket.reverse()
# >>> basket
# ['c', 'r', 'b', 'a']
# >>> basket.sort()
# >>> basket
# ['a', 'b', 'c', 'r']
# >>> basket
# ['a', 'b', 'c', 'r']
# >>> new_basket = sorted(basket)
# >>> new_basket
# ['a', 'b', 'c', 'r']
# >>> new_basket[len(new_basket):len(new_basket)]
# []
# >>> new_basket
# ['a', 'b', 'c', 'r']
# >>> new_basket[len(new_basket)] = len(new_basket) Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list assignment index out of range
# >>> new_basket.append(len(new_basket))
# >>> new_basket
# ['a', 'b', 'c', 'r', 4]
# >>> #importante tener presente cuando se modifican la lista en el mismo lugar o cuando es una copia >>> phrase = '-'.join(new_basket)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: sequence item 4: expected str instance, int found
# >>> new_basket.pop()
# 4
# >>> phrase = '-'.join(new_basket)
# >>> phrase
# 'a-b-c-r'
# >>> #convert list into a string
# >>> #list unpacking
# >>> a,b,c = [2,3,4]
# >>> a
# 2
# >>> a,v,c,*other = [2,3,4,5,5,6]
# >>> a
# 2
# >>> other
# [5, 5, 6]
# >>> a,v,c,*other,f = [2,3,4,5,5,6]
# >>> f
# 6
# >>> #dictionary
# >>> my_list = [
# ... {'a':[12,3,4], 'b':[2,3,4]},
# ... {'uno': 1, 'two':[2,3]
# ... ]
#   File "<stdin>", line 4
#     ]
#     ^
# SyntaxError: closing parenthesis ']' does not match opening parenthesis '{' on line 3
# >>> #key debe ser unica e inmutable
# >>> user = dict(name='hi')
# >>> user
# {'name': 'hi'}
# >>> 'hi' in user.values()
# True
# >>> user2 = user.copy()
# >>> user2
# {'name': 'hi'}
# >>> user2.clear()
# >>> user2
# {}
# >>> user
# {'name': 'hi'}
# >>> user.update({'age':20})
# >>> user
# {'name': 'hi', 'age': 20}
# >>> #tuples
# >>> points = 82,3)
#   File "<stdin>", line 1
#     points = 82,3)
#                  ^
# SyntaxError: unmatched ')'
# >>> points = (82,3)
# >>> 3 in points
# True
# >>> a,b =(1,3)
# >>> a
# 1
# >>> b
# 3
# >>> (a,b) = (b,a)
# >>> a
# 3
# >>> b
# 1
# >>> (a,b) = (b,a)
# >>> a
# 1
# >>> b
# 3
# >>> x,y,*b = (1,2,3,4)
# >>> x
# 1
# >>> b
# [3, 4]
# >>> points.count()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: tuple.count() takes exactly one argument (0 given)
# >>> points
# (82, 3)
# >>> points.count()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: tuple.count() takes exactly one argument (0 given)
# >>> points.count(1)
# 0
# >>> points.count(3)
# 1
# >>> len(points)
# 2
# >>> points[:]
# (82, 3)
# >>> #sets
# >>> new_set = {11,11,2,3}
# >>> new_set
# {11, 2, 3}
# >>> new_set.add(4)
# >>> new_set.add([2,3])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# >>> new_set.add((2,3))
# >>> new_set
# {2, 3, 4, 11, (2, 3)}
# >>> 3 in new_set
# True
# >>> len(new_set)
# 5
# >>> list_copy = list(new_set)
# >>> list_copy
# [2, 3, 4, 11, (2, 3)]
# >>> copy_set = new_set.copy()
# >>> copy_set
# {(2, 3), 2, 3, 4, 11}
# >>> my_set = {1,2,3,4,5}
# >>> your_set = {4,5,6,7,8,9,10}
# >>> my_set.difference(your_set)
# {1, 2, 3}
# >>> my_set.discard(5)
# >>> my_set
# {1, 2, 3, 4}
# >>> my_set.difference_update(your_set)
# >>> my_set
# {1, 2, 3}
# >>> my_set.intersection(your_set)
# set()
# >>> my_set
# {1, 2, 3}
# >>> #conditionals, truthy falsy, ternary operator >>> #condition_if_true if condition else cond_if_false
# >>> number = False
# >>> number + 2 if number else 'not a number'
# 'not a number'
# >>> number = True
# >>> number + 2 if number else 'not a number'
# 3
# >>> #short circuiting
# >>> #logical operators
# >>> True == 1
# True
# >>> '' == 1
# False
# >>> [] == []
# True
# >>> [1,2] == [1,2]
# True
# >>> '1' == 1
# False
# >>> [1,2] is [1,2]
# False
# >>> for item in 'hola':
# ...  print(len(item)-1*'*')
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# TypeError: unsupported operand type(s) for -: 'int' and 'str'
# >>>  print((len(item)-1)*'*')
#   File "<stdin>", line 1
#     print((len(item)-1)*'*')
# IndentationError: unexpected indent
# >>> for item in 'hola':
# ...   print((len(item)-1)*'*'))
#   File "<stdin>", line 2
#     print((len(item)-1)*'*'))
#                             ^
# SyntaxError: unmatched ')'
# >>>
# >>> for item in 'hola':
# ...   print((len('hola')-1)*'*')
# ...
# ***
# ***
# ***
# ***
# >>> for item in (1,2,3):
# ...   print(item)
# ... print('item:',item)
#   File "<stdin>", line 3
#     print('item:',item)
#     ^^^^^
# SyntaxError: invalid syntax
# >>> for item in (1,2,3):
# ...   print(item)
# ...
# 1
# 2
# 3
# >>> item
# 3
# >>> for item in (1,2,3):
# ...   for letter in ['a','b','e']:
# ...     print(item, letter)
# ...
# 1 a
# 1 b
# 1 e
# 2 a
# 2 b
# 2 e
# 3 a
# 3 b
# 3 e
# >>> #iterar en diccionarios
# >>> user = {
# ... 'name': 'juan',
# ... 'age':28
# ... }
# >>> for item in user.items():
# ...   print(item)
# ...
# ('name', 'juan')
# ('age', 28)
# >>> for name, age in user.items():
# ...   print(name, age)
# ...
# name juan
# age 28
# >>> for name in user.items():
# ...   print(name)
# ...
# ('name', 'juan')
# ('age', 28)
# >>> for item in user.values():
# ...   print(item)
# ...
# juan
# 28
# >>> for item in user.keys():
# ...   print(item)
# ...
# name
# age
# >>> for item in user.items():
# ...   k,v = item
# ...   print(k,v)
# ...
# name juan
# age 28
# >>> for _ in range(10):
# ...  print(_)
# ...
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# >>> for _ in range(10):
# ...  print(list(range(4))
# ...
# ...
# ...
# ...
# ...  break
#   File "<stdin>", line 7
#     break
#     ^^^^^
# SyntaxError: invalid syntax
# >>> for _ in range(0,10,2):
# ...   print(list(range(_))
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ... break
#   File "<stdin>", line 17
#     break
#     ^^^^^
# SyntaxError: invalid syntax
# >>> for _ in range(2):
# ...   print(list(range(10)))
# ...
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> #Enumerate
# >>> for i,char in enumerate('hola'):
# ...   print(i, char)
# ...
# 0 h
# 1 o
# 2 l
# 3 a
# >>> for i,char in enumerate(list(range(100))):
# ...   if char == 50:
# ...     print(i)
# ...
# 50
# >>> while 0 > 10:
# ...     print(i)
# ...   break
#   File "<stdin>", line 3
#     break
#          ^
# IndentationError: unindent does not match any outer indentation level
# >>> i= 0
# >>> while i<40:
# ...   print(i)
# ...   i += 2
# ...
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28
# 30
# 32
# 34
# 36
# 38
# >>> i = 0
# >>> while i < 40:
# ...  print(i)
# ...  i += 1
# ...  break
# ... else:
# ...  print('hi')
# ...
# 0
# >>> #loops break y continue
# >>> for item in 'hi':
# ...  pass
# ...
# >>> [0,0] + [1] + [0,0]
# [0, 0, 1, 0, 0]
# >>> def create_Zero_list:
#   File "<stdin>", line 1
#     def create_Zero_list:
#                         ^
# SyntaxError: expected '('
# >>> def create_Zero_list(number):
# ...   str = '0'*number
# ...   n = ''.join(str)
# ...   return n
# ...
# >>> create_Zero_list(2)
# '00'
# >>> create_Zero_list(5)
# '00000'
# >>> def create_zero_list(number):
# ...   str = '0'*number
# ...   str = ''.split
# ...    break
#   File "<stdin>", line 4
#     break
# IndentationError: unexpected indent
# >>> def create_zero_list(number):
# ...   str = '0'*number
# ...   n = str.split()
# ...   return n
# ...
# >>> create_zero_list(2)
# ['00']
# >>> def create_list(number):
# ...   return [number*0  for i in range(number) ]
# ...
# >>> create_list(2)
# [0, 0]
# >>> def create_list_one(number):
# ...   return [ 1 for i in range(number)]
# ...
# >>> create_list_one(2)
# [1, 1]
# >>> a = create_list(3) + create_list_one(1) + create_list(3)
# >>> a
# [0, 0, 0, 1, 0, 0, 0]
# >>> for i in range(6):
# ...  break
# ...  print(i)
# ... breal
#   File "<stdin>", line 4
#     breal
#     ^^^^^
# SyntaxError: invalid syntax
# >>> picture = []
# >>> for i in range(6):
# ...   hj
# ... ss
#   File "<stdin>", line 3
#     ss
#     ^^
# SyntaxError: invalid syntax
# >>> picture
# []
# >>> a
# [0, 0, 0, 1, 0, 0, 0]
# >>> b = create_list(2)+create_list_one(3)+create_list(2)
# >>> b
# [0, 0, 1, 1, 1, 0, 0]
# >>> c = create_list(1) + create_list_one(6)+create_list(1)
# >>> c
# [0, 1, 1, 1, 1, 1, 1, 0]
# >>> a
# [0, 0, 0, 1, 0, 0, 0]
# >>> b
# [0, 0, 1, 1, 1, 0, 0]
# >>> c
# [0, 1, 1, 1, 1, 1, 1, 0]
# >>> d = create_list_one(7)
# >>> d
# [1, 1, 1, 1, 1, 1, 1]
# >>> e = create_list(3)+create_list_one(1)+create_list(3)
# >>> e
# [0, 0, 0, 1, 0, 0, 0]
# >>> f = e
# >>> f = e[:]
# >>> f
# [0, 0, 0, 1, 0, 0, 0]
# >>> for i in range(6):
# ...   df
# ... s
#   File "<stdin>", line 3
#     s
#     ^
# SyntaxError: invalid syntax
# >>> sub_arrays = ('a','b','c','d','e','f')
# >>> for i in sub_arrays:
# ...   picture.append(i)
# ...
# >>> picture
# ['a', 'b', 'c', 'd', 'e', 'f']
# >>> a
# [0, 0, 0, 1, 0, 0, 0]
# >>> sub_arrays = (a,b,c,d,e,f)
# >>> picture.clear()
# >>> picture
# []
# >>> sub_arrayas
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'sub_arrayas' is not defined. Did you mean: 'sub_arrays'?
# >>> sub_arrays
# ([0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0])
# >>> for i in sub_arrays:
# ...   picture.append(i)
# ...
# >>> picture
# [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]
# >>> for outer in picture:
# ...   for inner in outer:
# ...      if inner == 0:
# ...        print(" ",end="")
# ...      else: print("*", end="")
# ... print()
#   File "<stdin>", line 6
#     print()
#     ^^^^^
# SyntaxError: invalid syntax
# >>> for outer in picture:
# ...   for inner in outer:
# ...      if inner == 0:
# ...        print(" ",end="")
# ...      else: print("H",end="")
# ...   print()
# ...
#    H
#   HHH
#  HHHHHH
# HHHHHHH
#    H
#    H
# >>>