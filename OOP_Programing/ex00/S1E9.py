from abc import ABC, abstractmethod
class Character(ABC):

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        pass

    @abstractmethod
    def do_not_do_it(self):
        pass
    
    def __str__(self):
        me = "good"
        if self.is_alive == False:
            me = "in haven"
        return f"My name is {self.first_name} a I'm {me}"

class Strong(Character):

    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

    def do_not_do_it(self):
        self.is_alive == False 

def main():

    x = Strong("PEPE")
    print(x)
    x.do_not_do_it()
    print(x)
    y = Strong("PIPOPOPOROPO", False)
    print(y)
   

if __name__ == "__main__":
    main()