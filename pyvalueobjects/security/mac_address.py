import re

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class MacAddress(NonEmptyString):

    __MATCHER = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')

    def __init__(self, value: str):
        super().__init__(value)

    def _validate(self, value: str):
        super()._validate(value)
        try:
            is_correct = MacAddress.__MATCHER.match(value)
            if not is_correct:
                raise ValueObjectError('Value must be a valid MAC address format (e.g. 00:1A:2B:3C:4D:5E or 00-1A-2B-3C-4D-5E).')
        except ValueError:
            raise ValueObjectError('Value must be a valid MAC address format (e.g. 00:1A:2B:3C:4D:5E or 00-1A-2B-3C-4D-5E).') 