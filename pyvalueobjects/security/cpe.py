import re

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.non_empty_string import NonEmptyString


class Cpe(NonEmptyString):

    __MATCHER = re.compile(
        r'^cpe:/[aho]:[-a-zA-Z0-9._~%:@!$&\'()*+,;=]+(:[-a-zA-Z0-9._~%:@!$&\'()*+,;=]+)*(:[a-zA-Z0-9._~%:@!$&\'()*+,;=]'
        r'+)*(:[a-zA-Z0-9._~%:@!$&\'()*+,;=]+)*(:[a-zA-Z0-9._~%:@!$&\'()*+,;=]+)*(:[a-zA-Z0-9._~%:@!$&\'()*+,;=]+)*$')

    def __init__(self, value):
        super().__init__(value)

    def _validate(self, value: str):
        super()._validate(value)
        try:
            is_correct = Cpe.__MATCHER.match(value)
            if not is_correct:
                raise ValueObjectError('Value must be valid a CPE format strings.')
        except ValueError:
            raise ValueObjectError('Value must be valid a CPE format strings.')
