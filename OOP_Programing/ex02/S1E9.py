from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        """
        Return a string representation of the character.
        """
        f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
        return self.__str__()
    
    @abstractmethod
    def do_not_do_it(self):
        pass
    
class Stark(Character):
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
        super().__init__(first_name, is_alive)

    def do_not_do_it(self):
        """
        do_not_do_it():
        Set is_alive attribute to False.
        """
        self.is_alive = False 
