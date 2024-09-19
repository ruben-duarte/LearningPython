# >>> name = input("your name")                     
# your name rub                                     
# >>> print('hello',name)                           
# hello  rub                                        
# >>> python ="""                                   
# ... source code => interpreter => bytecode => runs
# virtual machine => executes top down left right //
# se ejecuta el codigo en el ultimo momento """     
# >>> python                                        
# '\nsource code => interpreter => bytecode => runsv
# irtual machine => executes top down left right //s
# e ejecuta el codigo en el ultimo momento '        
# >>> """ data types                                
# ... int                                           
# ... float                                         
# ... bool                                          
# ... str                                           
# ... list                                          
# ... tuple                                         
# ... set                                           
# ... dict                                          
# ...                                               
# ... custom types -> classes                       
# ... specialized data types -> modules,packages fro
# m libreries                                       
# ... None                                          
# ... "                                             
# ... """                                           
# ' data types\nint\nfloat\nbool\nstr\nlist\ntuple\n
# set \ndict\n\ncustom types -> classes\nspecialized
#  data types -> modules,packages from libreries\nNo
# ne\n"\n'                                          
# >>> print(type(3+4))                              
# <class 'int'>                                     
# >>> add = 3+4                                     
# >>> print(id(add))                                
# 140717839733736                                   
# >>> bool(add)                                     
# True                                              
# >>> b = add                                       
# >>> print(type(b))                                
# <class 'int'>                                     
# >>> b = 3                                         
# >>> print(type(b))                                
# <class 'int'>                                     
# >>> b                                             
# 3                                                 
# >>> add                                           
# 7                                                 
# >>> 10/2                                          
# 5.0                                               
# >>> 10//2                                         
# 5                                                 
# >>> 1/2 +1/2                                      
# 1.0                                               
# >>> 10%2                                          
# 0                                                 
# >>> b                                             
# 3                                                 
# >>> a = 10.7                                      
# >>> a                                             
# 10.7                                              
# >>> bin(b)                                        
# '0b11'                                            
# >>> bin(a)                                        
# Traceback (most recent call last):                
#   File "<stdin>", line 1, in <module>             
# TypeError: 'float' object cannot be interpreted as
#  an integer                                       
# >>> 2 ** 3                                        
# 8                                                 
# >>> 2 ** 3 ** 4                                   
# 2417851639229258349412352                         
# >>> 2 // 4                                        
# 0                                                 
# >>> 5 // 4 // 2                                   
# 0                                                 
# >>> 12 // 2 // 3                                  
# 2                                                 
# >>> 5 % 4                                         
# 1                                                 
# >>> round(3.8)                                    
# 4                                                 
# >>> round(3.5)                                    
# 4                                                 
# >>> abs(-2)                                       
# 2                                                 
# >>> abs(-2i)                                      
#   File "<stdin>", line 1                          
#     abs(-2i)                                      
#          ^                                        
# SyntaxError: invalid decimal literal              
# >>> 2i                                            
#   File "<stdin>", line 1                          
#     2i                                            
#     ^                                             
# SyntaxError: invalid decimal literal              
# >>> 2*i                                           
# Traceback (most recent call last):                
#   File "<stdin>", line 1, in <module>             
# NameError: name 'i' is not defined. Did you mean: 
# 'id'?                                             
# >>> #Math functions                               
# >>> #operator precedence                          
# >>> (30-4) + 4*5                                  
# 46                                                
# >>> 30-4+4*5                                      
# 46                                                
# >>> 30-(4 + 4*5)                                  
# 6                                                 
# >>> # ()  **   * /  + -                           
# >>> bin(5)                                        
# '0b101'                                           
# >>> int('0b101',2)                                
# 5                                                 
# >>> 3*j                                           
# Traceback (most recent call last):                
#   File "<stdin>", line 1, in <module>             
# NameError: name 'j' is not defined                
# >>> 3j                                            
# 3j                                                
# >>> abs(-2j)                                      
# 2.0                                               
# >>> #variable  assign = operator means  <-  bindin
# g vincular                                        
# >>> lifes = 100                                   
# >>> lifes                                         
# 100                                               
# >>> #constants                                    
# >>> PI = 3.1415                                   
# >>> ab,b,c =1,2,3                                 
# >>> ab                                            
# 1                                                 
# >>> #expresion produce un valor, statement una lin
# ea completa de codigo que realiza una accion      
# >>> iq = 100                                      
# >>> user_age = iq / 4                             
# >>> user_age                                      
# 25.0                                              
# >>> #augmented assigment operator                 
# >>> temp = 80                                     
# >>> temp += 2                                     
# >>> temp                                          
# 82                                                
# >>> #strings                                      
# >>> user = 'john'                                 
# >>> hi = '''                                      
# ... WoW                                           
# ... 000                                           
# ... ---                                           
# ... '''                                           
# >>> hi                                            
# ' \nWoW\n000\n---\n'                              
# >>> #concatenation                                
# >>> hi + user                                     
# ' \nWoW\n000\n---\njohn'                          
# >>> str(30)                                       
# '30'                                              
# >>> #escape sequence                              
# >>> hi = "\t hello\"tu"                           
# >>> hi                                            
# '\t hello"tu'                                     
# >>> #formatted strings                            
# >>> #indexing [start:stop:step]                   
# >>> #strings are inmutable                        
# >>> #built in functions in python                 
# >>> #writing comments in python check real python 
# >>> #lists are mutable                            
# >>> #list slicing create a new copy               