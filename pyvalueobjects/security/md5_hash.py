import re

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class Md5Hash(NonEmptyString):

    __MATCHER = re.compile(r'^[a-fA-F0-9]{32}$')

    def __init__(self, value: str):
        super().__init__(value)

    def _validate(self, value: str):
        super()._validate(value)
        try:
            is_correct = Md5Hash.__MATCHER.match(value)
            if not is_correct:
                raise ValueObjectError('Value must be a valid MD5 hash (32 hexadecimal characters).')
        except ValueError:
            raise ValueObjectError('Value must be a valid MD5 hash (32 hexadecimal characters).') 