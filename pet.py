from datetime import datetime

class Pet:
    
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        self.commands = []
        self.date_of_birth = None

    def add_command(self, command):
        
        self.commands.append(command)

    def show_commands(self):
        
        if self.commands:
            print(f"Команды, которые умеет {self.name}:")
            for command in self.commands:
                print(f"- {command}")
        else:
            print(f"{self.name} пока не умеет никаких команд.")

    def get_info(self):
        
        info = f"Имя: {self.name}\n"
        info += f"Тип: {self.pet_type}\n"
        if self.date_of_birth:
            info += f"Дата рождения: {self.date_of_birth.strftime('%Y-%m-%d')}\n"
        info += "Команды:\n"
        self.show_commands()
        return info 

class Dog(Pet):
    

    def __init__(self, name, breed):
        super().__init__(name, "Собака")
        self.breed = breed

class Cat(Pet):
    

    def __init__(self, name):
        super().__init__(name, "Кошка")



    