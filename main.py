from pet import Pet, Dog, Cat
from counter import Counter
from datetime import datetime

class Main:
    def __init__(self):
        self.pets = []

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Завести новое домашнее животное")
            print("2. Посмотреть информацию о домашнем животном")
            print("3. Обучить домашнее животное")
            print("4. Выйти")

            choice = input("Введите номер действия: ")

            if choice == "1":
                self.add_pet()
            elif choice == "2":
                self.show_pet_info()
            elif choice == "3":
                self.train_pet()
            elif choice == "4":
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")

    def add_pet(self):
        with Counter() as counter:  # Используем try-with-resources для Counter
            name = input("Введите имя животного: ")
            pet_type = input("Введите вид животного (собака/кошка): ")

            if pet_type.lower() == "собака":
                breed = input("Введите породу собаки: ")
                pet = Dog(name, breed)
            elif pet_type.lower() == "кошка":
                breed = input("Введите породу кошки: ")
                pet = Cat(name)
            
            else:
                print("Неверный вид животного. Доступны: собака/кошка")
                return  # Выходим из функции, если тип неверный

            date_str = input("Введите дату рождения (дд.мм.гггг): ")
            try:
                day, month, year = map(int, date_str.split('.'))
                pet.date_of_birth = datetime(year, month, day)
                self.pets.append(pet)
                counter.add()  # Увеличиваем счетчик, если все поля заполнены
                print(f"Животное {pet.name} добавлено!")
            except ValueError:
                print("Неверный формат даты рождения. Введите дату в формате дд.мм.гггг")

    def show_pet_info(self):
        if self.pets:
            for i, pet in enumerate(self.pets):
                print(f"{i + 1}. {pet.name} ({pet.pet_type})")
            index = int(input("Введите номер животного: ")) - 1
            if 0 <= index < len(self.pets):
                print(self.pets[index].get_info())
            else:
                print("Неверный номер животного.")
        else:
            print("В реестре нет домашних животных.")

    def train_pet(self):
        if self.pets:
            for i, pet in enumerate(self.pets):
                print(f"{i + 1}. {pet.name} ({pet.pet_type})")
            index = int(input("Введите номер животного: ")) - 1
            if 0 <= index < len(self.pets):
                command = input("Введите новую команду: ")
                self.pets[index].add_command(command)
                print(f"Команда '{command}' добавлена для {pets[index].name}!")
            else:
                print("Неверный номер животного.")
        else:
            print("В реестре нет домашних животных.")


if __name__ == "__main__":
    main_app = Main()
    main_app.run()
    
    
    