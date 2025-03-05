import re

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class EmailAddress(NonEmptyString):

    __MATCHER = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    def __init__(self, value: str):
        super().__init__(value)

    def _validate(self, value: str):
        super()._validate(value)
        try:
            is_correct = EmailAddress.__MATCHER.match(value)
            if not is_correct:
                raise ValueObjectError('Value must be a valid email address format (e.g. user@example.com).')
        except ValueError:
            raise ValueObjectError('Value must be a valid email address format (e.g. user@example.com).') 