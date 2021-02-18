class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        if isinstance(self, PoliceCar):
            self.is_police = True

    def go(self):
        print(f'{self.name} is running')

    def stop(self):
        print(f'{self.name} is stop')

    def turn(self, direction):
        print(f'{self.name} is turn {direction}')

    def show_speed(self):
        print(f'{self.name} is current speed: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} is town car! Max speed is 60')

        else:
            print(f'{self.name} is current speed: {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} is work car! Max speed is 40')

        else:
            print(f'{self.name} is current speed: {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


cars = [TownCar(80, 'Red', 'Jimmy'), \
        SportCar(240, 'Yellow', 'Ferrary'), \
        WorkCar(50, 'Green', 'Cat'), \
        PoliceCar(100, 'White', 'Ford')]

for el in cars:
    print(f'Color {el.name} is {el.color}')
    print(f'Does is {el.name} police car?\n{el.is_police}')
    el.go()
    el.stop()
    el.turn('right')
    el.show_speed()