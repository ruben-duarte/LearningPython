class PlayerRugby:
    membership = True #CLass Attribute is static
    def __init__(self,name='anonimus', age=0):#constructor
        if self.age > 18:     
            self.name = name
            self.age = age

    def run(self):
        print('running')

    def shout(self):
        print(f'hey! my name is {self.name }!!!')
        #always put self
    
    @classmethod
    def add_numbers(num1,num2):
        return num1 + num2

p_3 = PlayerRugby('charles',30) # due default age it doesnt instantiate
p_3.shout()
p_3.add_numbers(2,4)