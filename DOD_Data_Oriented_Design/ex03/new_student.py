import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname
        self.login = self.name[0] + self.surname
        self.id = generate_id()

    def __str__(self) -> str:
        return f"Student(name={self.name}, surname={self.surname}, active=Tru login={self.login}, id={self.id})"
    