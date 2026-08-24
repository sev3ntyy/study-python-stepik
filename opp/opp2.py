class Cat:
    def __init__(self):
        self.state = "спит"
    def get_state(self):
        return self.state

class Book:
    def __init__(self,title):
        self.title = title
    def get_title(self):
        return self.title    


class User:
    def __init__(self,username,age):
        self.username = username 
        self.age = age
    def get_info(self):
        return f"Имя: {self.username}, Возраст: {self.age}"


class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        return f"{self.name} лает: Гав-гав!"


class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_total_price(self):
        return self.price * self.quantity


class Note:
    def __init__(self,text,tags):
        self.text = text
        self.tags = tags

class GameConfig:
    MAX_LEVEL = 100
    SERVER_NAME = "Stepik-RPG"


class Character:
    character_count = 0 
    def __init__(self,name):
        self.name = name
        Character.character_count = Character.character_count + 1 


class Employee:
    company = "Stepik"
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"{self.name} работает в компании {Employee.company} на должности {self.position}."


class Config:
    theme = "light"
    def __init__(self,app_name):
        self.app_name = app_name
    def get_theme(self):
        return self.theme












