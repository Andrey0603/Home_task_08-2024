class Animals:
    def __init__(self, name):
        self.__name = name  

    def get_name(self):
        return self.__name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Home_Animals(Animals):
    def speak(self):
        return f"{self.get_name()} издает звук!"


class Dog(Home_Animals):
    def speak(self):
        return f"{self.get_name()} издает звук: Гав!"


class Cat(Home_Animals):
    def speak(self):
        return f"{self.get_name()} издает звук: Мяу!"


class Hamster(Home_Animals):
    def speak(self):
        return f"{self.get_name()} издает звук: Пии!"


class Pack_Animals(Animals):
    def speak(self):
        return f"{self.get_name()} издает звук!"


class Horse(Pack_Animals):
    def speak(self):
        return f"{self.get_name()} издает звук: Иго-го!"


class Camel(Pack_Animals):
    def speak(self):
        return f"{self.get_name()} издает звук: Уу-ху!"


class Donkey(Pack_Animals):
    def speak(self):
        return f"{self.get_name()} издает звук: Иа-иа!"
    
    
dog = Dog("Рекс")
print(dog.speak())

cat = Cat("Мурка")
print(cat.speak())

horse = Horse("Гроза")
print(horse.speak())    