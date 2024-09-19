# >>> a = 6
# >>> a
# 6
# >>> a = 'hello'
# >>> a
# 'hello'
# >>> #la variable apunta al objeto asignado
# >>> #y asi sabe que tipo de datos es
# >>> #en run time : tiempo de ejecución
# >>> len(a)
# 5
# >>> A
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'A' is not defined. Did you mean: 'a'?
# >>> #uppercase sensitive, si no existe manda un error
# >>> #no asume un valor vacio o indefinido como en otros lenguajes
# >>> #el interprete permite realizar experimentos
# >>> 'hello' + 3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# >>> quit
# Use quit() or Ctrl-Z plus Return to exit
# >>> import sys
# >>> dir(sys)

# >>> len
# <built-in function len>
# >>> #hace referencia a la funcion
# >>>

# >>> a = 'hey'
# >>> a = "isn't"
# >>> len(a)
# 5
# >>> a + 'wow'
# "isn'twow"
# >>> a
# "isn't"
# >>> #strings son inmutables, siempre crea nuevos strings
# >>> a.lower()
# "isn't"
# >>> a.upper()
# "ISN'T"
# >>> a
# "isn't"
# >>> #ejecuta este metodo upper en el objeto a
# >>> a.find('e')
# -1
# >>> a.find('i')
# 0
# >>> a[0]
# 'i'
# >>> a[-1]
# 't'
# >>> a[10]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# >>> 'Hi %s I have %d ballons' % ('chris', 42)
# 'Hi chris I have 42 ballons'
# >>> #revisar como python maneja unicode
# >>> #los strings son una secuencia de bytes
# >>> a[1:2]
# 's'
# >>> a[1:4]
# "sn'"
# >>> a[1:5:2]
# "s'"
# >>> a[1:]
# "sn't"
# >>> a[:]
# "isn't"
# >>> #python tiene otra numeracion para indexar con numeros negativos pensando en representar len - num
# >>> a[-4:-2]
# 'sn'
# >>> a[:-3]
# 'is'
# >>> a[-3:]
# "n't"

"""
    python utiliza indentacion, tener cuidado con espacios y tabs. preferir espacios.
"""

# >>> a = [1,2,3*
# ...
# ... ]
#   File "<stdin>", line 3
#     ]
#     ^
# SyntaxError: invalid syntax
# >>> a = [1,2,3]
# >>> a
# [1, 2, 3]
# >>> # sintaxis consistente para listas, strings
# >>> len(a)
# 3
# >>> a + [2,4]
# [1, 2, 3, 2, 4]
# >>> a = [1,2,3]
# >>> b = a
# >>> a
# [1, 2, 3]
# >>> b
# [1, 2, 3]
# >>> a[0]
# 1
# >>> a[0] = 7
# >>> a
# [7, 2, 3]
# >>> b
# [7, 2, 3]
# >>> #al modificar a se modifico b, b = a no es una copia, la lista es mutable
# >>> b = a[:]
# >>> # ahora si es una copia, antes ambas variables apuntaban al mismo objeto
# >>> a == b
# True
# >>> a
# [7, 2, 3]
# >>> a[1:3]
# [2, 3]
# >>> a[:-1]
# [7, 2]
# >>> for num in a: print(num)
# ...
# 7
# 2
# 3
# >>> 3 in a
# True
# >>> a.append(4)
# >>> a
# [7, 2, 3, 4]
# >>> None
# >>> #append no regresa nada sino modifica en sitio

# >>> a.pop(0)
# 7
# >>> a
# [2, 3, 4]
# >>> del a
# >>> a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined
# >>> #borra la definicion de a
# >>> a = [1,2,3]
# >>> del a[1]
# >>> a
# [1, 3]
# >>> b = 14
# >>> a = b
# >>>
# >>> del a
# >>> a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined
# >>> b
# 14
# >>> #sorting
# >>> a = [2,5,3,4,]
# >>> sorted(a)
# [2, 3, 4, 5]
# >>> a
# [2, 5, 3, 4]
# >>> a.sort()
# >>> a
# [2, 3, 4, 5]
# >>> sorted(a, reverse=True)
# [5, 4, 3, 2]
# >>> #argumentos opcionales en sorted genera una nueva copia
# >>> #sobreescribir
# >>> a = sorted(a)
# >>> a
# [2, 3, 4, 5]
# >>> #custom sorted
# >>> a = ['cc','aaa','e']
# >>> sorted(a)
# ['aaa', 'cc', 'e']
# >>> # sort por longitud, two argument competitor technique en vez una key function en la lista original
# >>> len
# <built-in function len>
# >>> a
# ['cc', 'aaa', 'e']
# >>> sorted(a, key=len)
# ['e', 'cc', 'aaa']
# >>> a[1] = 'aaaau'
# >>> #sort por ultimo caracter
# >>> def last(s): return s[-1]
# ...
# >>> last
# <function last at 0x0000018901E45300>
# >>> sorted(a, key=last)
# ['cc', 'e', 'aaaau']
# >>> sorted(a, key=last, reverse=True)
# ['aaaau', 'e', 'cc']
# >>> #crear un string de una lista
# >>> ';'.join(a)
# 'cc;aaaau;e'
# >>> '\n'.join(a)
# 'cc\naaaau\ne'
# >>> b = ':'.join(a)
# >>> b
# 'cc:aaaau:e'
# >>> b.split(':')
# ['cc', 'aaaau', 'e']
# >>> result = []
# >>> for s in a: result.append(s)
# ...
# >>> result
# ['cc', 'aaaau', 'e']
# >>> range(14)
# range(0, 14)
# >>> for i in range(4): print(i)
# ...
# 0
# 1
# 2
# 3
# >>> #for loop en una lista no se puede modificar la estructura de la lista o su longitud mientras se recorre
# >>> #tupla
# >>> (1,2,3)
# (1, 2, 3)
# >>> #inmutable
# >>> a = (1,2,3)
# >>> len(a)
# 3
# >>> a[1*
# ...
# ...
# ... ]
#   File "<stdin>", line 4
#     ]
#     ^
# SyntaxError: invalid syntax
# >>> a[1]
# 2
# >>> a[1] = 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> #sort de una forma y luego de otra usar tuplas

# >>> a = [(1,"b"),(2,"a")]
# >>> #primero ordena por el primer item, si son iguales por el segundo
# >>> sorted(a)
# [(1, 'b'), (2, 'a')]
# >>> a
# [(1, 'b'), (2, 'a')]
# >>> a = [(1,"b"),(2,"a"),(1,"a")]
# >>> sorted(a)
# [(1, 'a'), (1, 'b'), (2, 'a')]
# >>> (x,y) = (1,2)
# >>> s
# 'e'
# >>> x
# 1
# >>> y
# 2
# >>>

# >>> #dict delimiter {}
# >>> d = {}
# >>> d['a'] = 'alpha'
# >>> d['o'] = 'omega'
# >>> d['g'] = 'gama'
# >>> # key retrive en tiempo constante o(n)
# >>> d['a']
# 'alpha'
# >>> d['x']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'x'
# >>> d.get('x')
# >>> d.get('a')
# 'alpha'
# >>> 'a' in d
# True
# >>> d
# {'a': 'alpha', 'o': 'omega', 'g': 'gama'}
# >>> 'alpha' in d
# False
# >>> d.keys()
# dict_keys(['a', 'o', 'g'])
# >>> # hashing en lista por loque estan en desorden

# >>> d.values()
# dict_values(['alpha', 'omega', 'gama'])
# >>> #loopin dict
# >>> for k in sorted(d.keys()): print('key:',k,'->',d[k])
# ...
# key: a -> alpha
# key: g -> gama
# key: o -> omega
# >>> d.items()
# dict_items([('a', 'alpha'), ('o', 'omega'), ('g', 'gama')])
# >>> for tuple in d.items(): print(tuple)
# ...
# ('a', 'alpha')
# ('o', 'omega')
# ('g', 'gama')
# >>>