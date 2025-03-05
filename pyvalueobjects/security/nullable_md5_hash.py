from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.security.md5_hash import Md5Hash

_nullable_cls = build_nullable(Md5Hash)


class NullableMd5Hash(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value) 