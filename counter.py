class Counter:
    

    def __init__(self):
        self.count = 0
        self.opened = False

    def add(self):
        
        self.count += 1

    def __enter__(self):
        self.opened = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.opened = False
        if exc_type is not None:
            print("Ошибка при работе с счетчиком!")
            return False
        if self.opened:
            raise Exception("Счетчик не был закрыт!")
        return True