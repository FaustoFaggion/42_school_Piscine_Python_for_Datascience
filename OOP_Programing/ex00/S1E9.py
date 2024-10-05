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
    """
    A class to represent a character in a story.
    Child class of Character class

    Attributes:
    ----------
    first_name : str
        The first name of the character.
    is_alive : bool
        A flag indicating if the character is alive (default is True).
    
    Methods:
    -------
    do_not_do_it():
        Set is_alive attribute to False.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        __init__(self, first_name: str, is_alive: bool = True):
        Instanciate a object and set the atributes acording to the paramters.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def do_not_do_it(self):
        """
        do_not_do_it():
        Set is_alive attribute to False.
        """
        self.is_alive == False 

def main():

    pepe = Strong("PEPE")
    print(pepe)
    print("\nStrong.__doc__:\n", pepe.__doc__)
    print("\n__init__.__doc__:\n", pepe.__init__.__doc__)
    print("\ndo_not_do_it.__doc__:\n", pepe.do_not_do_it.__doc__)
    pepe.do_not_do_it()
    print(pepe)
    y = Strong("PIPOPOPOROPO", False)
    print(y)
   

if __name__ == "__main__":
    main()