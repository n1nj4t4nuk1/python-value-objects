from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.security.url import Url

_nullable_cls = build_nullable(Url)


class NullableUrl(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value) 