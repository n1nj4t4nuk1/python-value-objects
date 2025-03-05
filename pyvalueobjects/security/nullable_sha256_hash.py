from pyvalueobjects.abstract.nullablevalueobject import build_nullable
from pyvalueobjects.security.sha256_hash import Sha256Hash

_nullable_cls = build_nullable(Sha256Hash)


class NullableSha256Hash(_nullable_cls):

    def __init__(self, value: str = None):
        super().__init__(value) 