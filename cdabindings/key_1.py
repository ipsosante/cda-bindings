from dataclasses import dataclass

from cdabindings.keybase import Keybase

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Key1(Keybase):
    class Meta:
        name = "key"
        namespace = "http://www.w3.org/2001/XMLSchema"
