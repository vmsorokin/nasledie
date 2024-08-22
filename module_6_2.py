class Vehicle:
        __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
        def __init__(self, owner, __model, __engine_power, __color):
            self.owner = owner
            self.__model = __model
            self.__engine_power = __engine_power
            self.__color = __color
        def get_model(self):
            print(f'Модель: {self.__model}')
        def get_horsepower(self):
            print(f'Мощность двигателя: {self.__engine_power}')
        def get_color(self):
            print(f'Цвет: {self.__color}')
        def print_info(self):
            self.get_model()
            self.get_horsepower()
            self.get_color()
            print(f'Владелец: {self.owner}')
        def set_color(self, new_colors):
            flag = True
            self.new_colors = new_colors
            for i in range(len(self.__COLOR_VARIANTS)):
                if self.__COLOR_VARIANTS[i].upper() == self.new_colors.upper():
                    self.__color = new_colors
                    flag = True
                    break
                else:
                    flag = False
                    continue
            if flag == False:
                print(f'Нельзя сменить цвет на {self.new_colors}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()