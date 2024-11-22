class House():
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor



    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"Название {self.name}, кол-во этажей: {self.number_of_floor}"



home_1 = House("ЖК Эльбрус", 10)
home_2 = House("ЖК Акация",20)



print(home_1)
print(home_2)
print(len(home_1))
print(len(home_2))