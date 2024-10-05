class User:
    def sign_in(self):
        print('logged in')

class Warrior(User):
    def __init__(self,name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with level of power {self.power}')

class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows ->, remaining arrows {self.num_arrows}')

warrior_1 = Warrior('Tom',34)
archer_1 = Archer('kim',33)
print(warrior_1.sign_in())
warrior_1.attack()
archer_1.attack()
archer_1.sign_in()

print(isinstance(warrior_1,Warrior))
"""
everuthing in py inherits from  object base class
"""
