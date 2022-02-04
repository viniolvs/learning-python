class Car():
    def __init__(self,make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year 

class EletricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year) #inicializa a classe filha com o contrutor da classe mae