from typing import List


class ValidationException(Exception):
    def __init__(self, errors: List[str]):
        self.errors = errors

    def __str__(self):
        return "Validation Exception:\n" + "\n".join(self.errors)
