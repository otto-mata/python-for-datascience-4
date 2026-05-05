import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a lowercase letters unique identifier, 15 letters long."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing a student."""

    name: str = field()
    surname: str = field()
    login: str = field(
        init=False,
    )
    active: bool = field(default=True)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Post init function, allowing the assignation of custom values
        after the initialization of the dataclass."""
        self.login = (
            self.name.lower()[0] + self.surname.lower().replace(" ", "-")
        )[:8]
