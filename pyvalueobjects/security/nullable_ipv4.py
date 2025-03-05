from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.security.ipv4 import Ipv4

_nullable_cls = build_nullable(Ipv4)


class NullableIpv4(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value) 