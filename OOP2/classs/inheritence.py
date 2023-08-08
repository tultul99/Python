#inheritence, overriding

class Bangladesh:
    def population(self):
        print('Population.')
    def area(self):
        print('Area.')

class Dhaka(Bangladesh):
    def capital(self):
        print('Capital.')

class Gazipur(Dhaka, Bangladesh):                  
    def IUT():
        print('IUT')

ob = Gazipur()
ob.population()
# s = Dhaka()
# s.population()
# s.area()
# s.capital()

class samsung:
    def __init__(self):
        print(f'Samsung class')

class vivo(samsung):
    def __init__(self):
        super().__init__()
        print(f'vivo class')

ob = vivo()
