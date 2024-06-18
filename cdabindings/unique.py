from dataclasses import dataclass

from cdabindings.keybase import Keybase

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Unique(Keybase):
    class Meta:
        name = "unique"
        namespace = "http://www.w3.org/2001/XMLSchema"
