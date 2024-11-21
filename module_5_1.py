class House():
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floor:
            for number in range(1, new_floor + 1):
                print(number)
        else:
            print("Такого этажа не существует")

home_1 = House("ЖК Краснодар", 30)
home_2 = House("ЖК Южный",25)
home_1.go_to(35)
home_2.go_to(15)

