class Player:
    membership = True #CLass Attribute is static
    def __init__(self,name, age):#constructor
        if self.membership:
            self.points = 100
        self.name = name #self:object not created yet
        self.age = age

    def run(self):
        print('running')

    def shout(self):
        print(f'hey! my name is {self.name }!!!')
        #always put self



p1 = Player('john', 33)
p1.membership
print(p1.points)
Player.membership
print(p1.shout())


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

p_3 = PlayerRugby() # due default age it doesnt instantiate
p_3.shout()
