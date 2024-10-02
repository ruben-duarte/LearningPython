class User:
    def sign_in(self):
        print('logged in')

class Warrior(User):
    pass

class Archer(User):
    pass

warrior_1 = Warrior()
print(warrior_1.sign_in())