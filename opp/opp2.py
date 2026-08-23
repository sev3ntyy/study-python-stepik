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





