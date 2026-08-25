class CourierRobot:
    service_name = "Python Delivery"
    total_robots = 0
    
    def __init__(self, name, max_energy):
        self.name = name
        self.max_energy = max_energy
        self.current_energy = 0
        self.delivered_orders = 0
        CourierRobot.total_robots += 1
    
    def charge(self, amount):
        if self.current_energy + amount <= self.max_energy:
            self.current_energy += amount
            print(f'{self.name}: получено {amount} ед. энергии')
        else:
            print(f"{self.name}: аккумулятор переполнен")
    
    def deliver(self, energy_cost):
        if self.current_energy >= energy_cost:
            self.current_energy -= energy_cost
            self.delivered_orders += 1
            print(f"{self.name}: заказ доставлен, потрачено {energy_cost} ед. энергии")
        else:
            print(f"{self.name}: недостаточно энергии")
    
    def show_info(self):
        print(f"Робот {self.name} | Служба: {self.service_name} | Энергия: {self.current_energy}/{self.max_energy} | Заказов: {self.delivered_orders}")
    
    def set_personal_service(self, service_name):
        self.service_name = service_name

name1 = input()
max_energy1 = int(input())
name2 = input()
max_energy2 = int(input())
charge1 = int(input())
charge2 = int(input())
deliver1 = int(input())
deliver2 = int(input())
new_service = input()
personal_service1 = input()

robot1 = CourierRobot(name1, max_energy1)
robot2 = CourierRobot(name2, max_energy2)


robot1.charge(charge1)
robot2.charge(charge2)

CourierRobot.service_name = new_service


robot1.set_personal_service(personal_service1)

robot1.deliver(deliver1)
robot2.deliver(deliver2)

robot1.show_info()
robot2.show_info()

print(f"Всего роботов: {CourierRobot.total_robots}")