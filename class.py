class Dog(): #modelando um cachorro
    def __init__(self,name,age): #contrutor
        self.name = name
        self.age = age
    def sit(self):
        print(self.name + " is now sitting.")

dog = Dog("Dori", 4)
dog.sit()


class Restaurant():
    def __init__(self,name, cuisine_type) -> None:
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.name, self.cuisine_type)
    def open_restaurant(self):
        print("The restaurant is open!")

my_r = Restaurant("oloco","hamburgueria")
my_r.describe_restaurant()
my_r.open_restaurant()

# HERANÇA
class Car():
    def __init__(self,make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year 

class EletricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year) #inicializa a classe filha com o contrutor da classe mae