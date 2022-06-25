from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    company: str = None
    email: str = None
    text_of_appeal: str = None