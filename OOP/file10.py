class User:
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('I"m  user !')

class Warrior(User):
    def __init__(self,name, power, email):
        super().__init__(self,email)
        self.name = name
        self.power = power
        
    def attack(self):
        super().attack() #using attack from parent
        print(f'attacking with level of power {self.power}')

class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows ->, remaining arrows {self.num_arrows}')

#polymorphism
w1 = Warrior('nick',70)
a1 = Archer('kim', 30)