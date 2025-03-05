import re

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class Ipv4(NonEmptyString):

    __MATCHER = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

    def __init__(self, value: str):
        super().__init__(value)

    def _validate(self, value: str):
        super()._validate(value)
        try:
            is_correct = Ipv4.__MATCHER.match(value)
            if not is_correct:
                raise ValueObjectError('Value must be a valid IPv4 address format (e.g. 192.168.1.1).')
        except ValueError:
            raise ValueObjectError('Value must be a valid IPv4 address format (e.g. 192.168.1.1).') 