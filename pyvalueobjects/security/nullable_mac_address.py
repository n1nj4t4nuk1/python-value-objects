from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.security.mac_address import MacAddress

_nullable_cls = build_nullable(MacAddress)


class NullableMacAddress(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value) 