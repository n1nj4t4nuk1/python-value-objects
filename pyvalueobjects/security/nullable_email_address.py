from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.security.email_address import EmailAddress

_nullable_cls = build_nullable(EmailAddress)


class NullableEmailAddress(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value) 