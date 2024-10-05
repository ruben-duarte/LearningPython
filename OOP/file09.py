class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('I"m  user !')

class Warrior(User):
    def __init__(self,name, power):
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

def player_attack(char):
    char.attack()

player_attack(w1)
player_attack(a1)

for player in [w1, a1]:
    player_attack(player)




