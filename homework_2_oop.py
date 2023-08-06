class Human:
 favorite_drink = 'bear'
 def __init__(self, age: 2):
     self.age = age
     if self.age < 18:
          self.favorite_drink = 'juice'
 def drink(self):
     name = self.__class__.__name__
     favorite_drink = self.favorite_drink
     print(f'{name} {self.age} likes {favorite_drink}')


Petya = Human(5)
Petya.drink()

Lena = Human(25)
Lena.drink()

class Worker(Human):
    def __init__(self, age, salary):
      super().__init__(age)
      self.salary = salary
      if self.age > 18 and salary > 1000:
          self.favorite_drink = 'wisky'


Sasha = Worker(7, 1500)
Sasha.drink()

Dima = Worker(19, 2500)
Dima.drink()

Borya = Worker(20, 300)
Borya.drink()



