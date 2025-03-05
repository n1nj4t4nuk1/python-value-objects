from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.security.ipv6 import Ipv6

_nullable_cls = build_nullable(Ipv6)


class NullableIpv6(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value) 