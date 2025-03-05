import re

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class Sha256Hash(NonEmptyString):

    __MATCHER = re.compile(r'^[a-fA-F0-9]{64}$')

    def __init__(self, value: str):
        super().__init__(value)

    def _validate(self, value: str):
        super()._validate(value)
        try:
            is_correct = Sha256Hash.__MATCHER.match(value)
            if not is_correct:
                raise ValueObjectError('Value must be a valid SHA256 hash (64 hexadecimal characters).')
        except ValueError:
            raise ValueObjectError('Value must be a valid SHA256 hash (64 hexadecimal characters).') 