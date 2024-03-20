class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor


    def __str__(self):
            if self.flavor:
                return f'У вас газировка с {self.flavor} вкусом'
            else:
                return 'У вас обычная газировка'



soda_one = Soda()
print(soda_one)



class Car:
    car_count = 0


    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

        Car.car_count += 1


    def display_info(self):
        print('Car:', self.color, self.type, self.year)


first_car = Car(color='red', type='sport', year=2000)
first_car.display_info()


print(Car.car_count)

second_car = Car(color='blue', type='grusovoy', year=2018)

def start(self):
    print(f'{self.type}заведена')

def stop(self):
    print(f'{self.type}остановилась')