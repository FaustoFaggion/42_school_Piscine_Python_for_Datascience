from S1E9 import Character

class Baratheon(Character):
    
    """Representing Baratheon family"""
    

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = 'dark'

    # def __str__(self):
    #     me = "good"
    #     if self.is_alive == False:
    #         me = "in haven"
    #     return f"My name is {self.first_name} a I'm {me}"
    
    @classmethod
    def create_baratheon(cls, first_name: str, is_alive: bool):
        obj = cls(first_name)
        obj.is_alive = is_alive
        return obj

    def do_not_do_it(self):
        self.is_alive = False

class Lannister(Character):
    
    """Representing Lannister family"""
    
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = 'light'

    # def __str__(self):
    #     me = "good"
    #     if self.is_alive == False:
    #         me = "in haven"
    #     return f"My name is {self.first_name} a I'm {me}"

    @classmethod
    def create_lannister(self, first_name: str, is_alive: bool = True):
        obj = Lannister(first_name)
        obj.is_alive = is_alive
        return obj
        
    def do_not_do_it(self):
        self.is_alive = False
