import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str = field()
    surname: str = field()
    login: str = field(
        init=False,
    )
    active: bool = field(default=True)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = (
            self.name.lower()[0] + self.surname.lower().replace(" ", "-")
        )[:8]
