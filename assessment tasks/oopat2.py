
class SpaceShip:
    agency = "Python Space"
    total_ships = 0

    def __init__(self, name, max_fuel):
        self.name = name                
        self.max_fuel = max_fuel
        self.current_fuel = 0

        SpaceShip.total_ships += 1        

    def refuel(self, amount):
        if self.current_fuel + amount > self.max_fuel:
            print(f"{self.name}: топливный бак переполнен")
        else:
            print(f"{self.name}: заправлено {amount} ед. топлива")
            self.current_fuel += amount

    def fly(self, fuel_cost):
        if self.current_fuel >= fuel_cost:
            self.current_fuel -= fuel_cost
            print(f"{self.name}: полет выполнен, потрачено {fuel_cost} ед. топлива")
        else:
            print(f"{self.name}: недостаточно топлива")

    def show_info(self):
        print(f"Корабль {self.name} | Агентство: {self.agency} | Топливо: {self.current_fuel}/{self.max_fuel}")

    def set_personal_agency(self, agency):
        self.agency = agency

ship1 = SpaceShip(input(), int(input()))

ship2 = SpaceShip(input(), int(input()))

 

ship1.refuel(int(input()))

ship2.refuel(int(input()))

 

ship1.fly(int(input()))

ship2.fly(int(input()))

 

SpaceShip.agency = input()

ship1.set_personal_agency(input())

 

ship1.show_info()

ship2.show_info()

 

print(f'Всего кораблей: {SpaceShip.total_ships}')



