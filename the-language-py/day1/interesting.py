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