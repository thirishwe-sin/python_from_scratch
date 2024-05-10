class Car:
    sterringWheel = 1 #class level attribute
    def __init__(self, name, wheel):
        self.name = name
        self.wheels = wheel #instance level attribute

    def drive(self):
        print(f'{self.name} is driving with {self.wheels} wheels')


    @classmethod
    def common(cls):
        print(f'all car has only {cls.sterringWheel} sterring wheel') #class level method


# marcedes = Car('Marcedes',4)
# marcedes.drive()

# print(Car.common())