from shared.exceptions import ValidationException


class ValidationService:
    __validators = []

    def __init__(self, validators) -> None:
        self.__validators = validators

    def add_validator(self, validator) -> None:
        self.__validators.append(validator)

    def validate(self) -> None:
        errors = []
        for validator in self.__validators:
            if validator[0]:
                errors.append(validator[1])

        if errors:
            raise ValidationException(errors=errors)
