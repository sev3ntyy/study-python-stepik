class CoffeeMachine:
    cafe_name = "Python Coffee"
    total_machines = 0
    
    def __init__(self, name, max_water):
        self.name = name
        self.max_water = max_water
        self.current_water = 0
        self.cups_made = 0
        CoffeeMachine.total_machines += 1
    
    def fill_water(self, amount):
        if self.current_water + amount <= self.max_water:
            self.current_water += amount
            print(f"{self.name}: добавлено {amount} ед. воды")
        else:
            print(f"{self.name}: бак переполнен")
    
    def make_coffee(self, water_cost):
        if self.current_water >= water_cost:
            self.current_water -= water_cost
            self.cups_made += 1
            print(f"{self.name}: кофе приготовлен, потрачено {water_cost} ед. воды")
        else:
            print(f"{self.name}: недостаточно воды")
    
    def show_info(self):
        print(f"Кофемашина {self.name} | Кофейня: {self.cafe_name} | Вода: {self.current_water}/{self.max_water} | Чашек: {self.cups_made}")
    
    def set_personal_cafe(self, cafe_name):
        self.cafe_name = cafe_name


name1 = input()
max_water1 = int(input())
name2 = input()
max_water2 = int(input())
water1 = int(input())
water2 = int(input())
coffee1 = int(input())
coffee2 = int(input())
new_cafe = input()
personal_cafe1 = input()

machine1 = CoffeeMachine(name1, max_water1)
machine2 = CoffeeMachine(name2, max_water2)

machine1.fill_water(water1)
machine2.fill_water(water2)

CoffeeMachine.cafe_name = new_cafe

machine1.set_personal_cafe(personal_cafe1)

machine1.make_coffee(coffee1)
machine2.make_coffee(coffee2)

machine1.show_info()
machine2.show_info()

print(f"Всего машин: {CoffeeMachine.total_machines}")