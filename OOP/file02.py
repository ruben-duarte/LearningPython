class Player:
    def __init__(self,name, age):#constructor
        self.name = name #self:object not created yet
        self.age = age

    def run(self):
        print('running')


p_1 = Player('james', 20)
p_2 = Player('Cindy', 22)

p_2.speed = 20
p_1.points = 100

print(p_1)
print(p_1.name)
print(p_2.name)

help(p_1)
help(list)       
        