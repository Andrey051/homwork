class House():
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor


    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor


    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor


    def __le__ (self, other):
        return self.number_of_floor <= other.number_of_floor


    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor


    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor


    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor


    def __add__(self, value):
        self.number_of_floor += value
        return self


    def __iadd__(self, value):
        return self + value


    def __radd__(self, value):
        return self + value



    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"Название {self.name}, кол-во этажей: {self.number_of_floor}"



home_1 = House("ЖК Эльбрус", 10)
home_2 = House("ЖК Акация",20)
isinstance(home_1, int)
isinstance(home_2, int)
isinstance(home_1, House)
isinstance(home_2, House)

print(home_1)
print(home_2)

print(home_1 == home_2) # eq

home_1 = home_1 + 10 # add
print(home_1)
print(home_1 == home_2)

home_1 += 10  # iadd
print(home_1)

home_2 = 10 + home_2 # raad
print(home_2)


print(home_1 > home_2) # gt
print(home_1 >= home_2) # ge
print(home_1 < home_2) # lt
print(home_1 <= home_2) # le
print(home_1 != home_2) # ne


