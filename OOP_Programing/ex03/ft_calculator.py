
class Calculator:

    def __init__(self, obj) -> None:
        self.obj = obj

    def __add__(self, object) -> None:
        tmp = [float(elem) + object for elem in self.obj]
        self.obj = tmp
        print(self.obj)

    def __mul__(self, object) -> None:
        tmp = [float(elem) * object for elem in self.obj]
        self.obj = tmp
        print(self.obj)

    def __sub__(self, object) -> None:
        tmp = [float(elem) - object for elem in self.obj]
        self.obj = tmp
        print(self.obj)
    
    def __truediv__(self, object) -> None:
        tmp = [float(elem) / object for elem in self.obj]
        self.obj = tmp
        print(self.obj)