#private public protected

class Player:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def run(self):
            print('running')
        
    def speak(self):
            print(f'Im {self._name}')

p_2 = Player('jena', 18)
p_2.run()
p_2.speak()

p_1 = Player('joseph', 30)
p_1.name = 'hh'
p_1.speak = 't'
p_1.speak()
p_2.speak()


