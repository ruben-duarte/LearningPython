class PlayerRugby:
    membership = True #CLass Attribute is static
    def __init__(self,name='anonimus',age=0):#constructor
        if age > 18:     #not sel.age
          self.name = name
          self.age = age

    def run(self):
        print('running')

    def shout(self):
        print(f'hey! my name is {self.name }!!!')
        #always put self
    
    @classmethod #can use it without instantiate
    def add_numbers(cls,num1,num2):
        #return num1 + num2
        return cls('Ted', num1+num2)
    
    #staticmethod is the same as classmethod but it
    #doesnt hace cls

print(PlayerRugby.add_numbers(2,2))
p_1 = PlayerRugby('charles',30) 
p_1.shout()
p_1.run()

print(p_1.add_numbers(2,7))